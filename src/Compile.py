from solcx import compile_standard, install_solc
import json

# Install the specified Solidity compiler version
install_solc("0.8.28")

# Read the Solidity contract file
with open("src/newContract.sol", "r") as file:
    contract_source = file.read()

# Compile the contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"newContract.sol": {"content": contract_source}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]}
            }
        },
    }
)

# Save compiled contract to a JSON file
with open("compiled.json", "w") as file:
    json.dump(compiled_sol, file)

print("Contract compiled successfully.")
