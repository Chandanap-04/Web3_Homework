from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
provider_url = os.getenv("http://127.0.0.1:8545")
private_key = os.getenv("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
account_address = os.getenv("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")

# Connect to the Anvil network
web3 = Web3(Web3.HTTPProvider(provider_url))
contract_address = "YOUR_DEPLOYED_CONTRACT_ADDRESS"  # Replace with actual address

# Load ABI
with open("compiled.json", "r") as file:
    compiled_sol = json.load(file)
abi = compiled_sol['contracts']['newContract.sol']['newContract']['abi']

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Update StudentId
nonce = web3.eth.get_transaction_count(account_address)
update_tx = contract.functions.updateID(5341).build_transaction({
    "chainId": 31337,
    "gasPrice": web3.to_wei("20", "gwei"),
    "from": account_address,
    "nonce": nonce,
})
signed_update_tx = web3.eth.account.sign_transaction(update_tx, private_key=private_key)
txn_hash = web3.eth.send_raw_transaction(signed_update_tx.rawTransaction)
web3.eth.wait_for_transaction_receipt(txn_hash)

# Retrieve updated StudentId
updated_id = contract.functions.viewMyId().call()
print(f"Updated value is {updated_id}")
