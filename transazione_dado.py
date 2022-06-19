import json
from web3 import Web3
import random

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


def extraction():
    return random.randint(1,6)


data={
    "address":['0x4c75beA232C817C2958827E77B408B4EAC63a1ec','0x248a0d6755CaF3d86ac0A114604750F348e2C586'],
    "private_key":['237e98efcdc46d0c4564ce495d36fb01a0b316fe2ba556e9fe73bfb4a857185b','63adfb23f7d5824f548221722a2603750ed36fcb180dd046a9af220cddc019b3'],
    "points":[]
}



for i in range(len(data["address"])):
    data["points"].append(extraction())


if data["points"][0]<data["points"][1]:
    nonce = web3.eth.getTransactionCount(data["address"][0])

    tx = {
        'nonce': nonce,
        'to': data["address"][1],
        'value': web3.toWei(1, 'ether'),
        'gas': 2000000,  # gas limit
        'gasPrice': web3.toWei('50', 'gwei'),
    }

    signed_tx = web3.eth.account.signTransaction(tx, data["private_key"][0])
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

else:
    nonce = web3.eth.getTransactionCount(data["address"][1])

    tx = {
        'nonce': nonce,
        'to': data["address"][0],
        'value': web3.toWei(1, 'ether'),
        'gas': 2000000,  # gas limit
        'gasPrice': web3.toWei('50', 'gwei'),
    }

    signed_tx = web3.eth.account.signTransaction(tx, data["private_key"][1])
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(data["points"])
print(web3.toHex(tx_hash))





