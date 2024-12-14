from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
private_key = os.getenv("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
provider_url = os.getenv("http://127.0.0.1:8545")
account_address = os.getenv("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")

# Connect to the local Anvil blockchain
web3 = Web3(Web3.HTTPProvider(provider_url))
chain_id = 31337

# Load compiled contract data
with open("compiled.json", "r") as file:
    compiled_sol = json.load(file)

# Extract ABI and bytecode
abi = compiled_sol['contracts']['newContract.sol']['newContract']['abi']
bytecode = compiled_sol['contracts']['newContract.sol']['newContract']['evm']['bytecode']['object']

# Create contract instance
contract = web3.eth.contract(abi=abi, bytecode=bytecode)

# Build deployment transaction
nonce = web3.eth.get_transaction_count(account_address)
transaction = contract.constructor().build_transaction({
    "chainId": chain_id,
    "gasPrice": web3.to_wei("20", "gwei"),
    "from": account_address,
    "nonce": nonce,
})

# Sign and send transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

print(f"Contract deployed at {txn_receipt.contractAddress}")
