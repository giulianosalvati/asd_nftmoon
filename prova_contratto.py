from web3 import Web3
from solcx import compile_source
import random
import json

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))


CONTRACT_SOL = 'TokenERC20.sol'
CONTRACT_NAME = 'simplestorage'


PRIVATE_KEY = "2fee9e1f29ddbafd9d8b7f93bd9c59fdba676880c69bc076cd5892be1ec76ece"
acct = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)

addr_2= "0xb87574d580ce21D77aea6dbfEf3B0305d42086A3"
contract_source_file="./contracts/TokenERC20.sol"

def compile_contract(contract_source_file, contractName=None):
    """
    Reads file, compiles, returns contract name and interface
    """
    with open(contract_source_file, "r") as f:
        contract_source_code = f.read()
    compiled_sol = compile_source(contract_source_code) # Compiled source code
    if not contractName:
        contractName = list(compiled_sol.keys())[0]
        contract_interface = compiled_sol[contractName]
    else:
        contract_interface = compiled_sol['<stdin>:' + contractName]
    return contractName, contract_interface

def deploy_contract(acct, contract_interface, contract_args=None):
    """
    deploys contract using self-signed tx, waits for receipt, returns address
    """
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    constructed = contract.constructor() if not contract_args else contract.constructor(*contract_args)
    tx = constructed.buildTransaction({
        'gasPrice': w3.eth.gas_price,
        'from': acct.address,
        'nonce': w3.eth.getTransactionCount(acct.address),
    })
    print ("Signing and sending raw tx ...")
    signed = acct.signTransaction(tx)
    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    print ("tx_hash = {} waiting for receipt ...".format(tx_hash.hex()))
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)
    contractAddress = tx_receipt["contractAddress"]
    print ("Receipt accepted. gasUsed={gasUsed} contractAddress={contractAddress}".format(**tx_receipt))
    return contractAddress

contractName, contract_interface = compile_contract(contract_source_file)
contract_address= deploy_contract(acct, contract_interface)
contract = w3.eth.contract(address=contract_address, abi=contract_interface['abi'])


balance = contract.functions.balanceOf(acct.address).call()/10**18
print(f"Balance: {balance}")

