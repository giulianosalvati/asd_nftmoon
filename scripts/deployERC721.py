from lib2to3.pgen2 import token
from brownie import Contract, DiceNFT, accounts
from web3 import Web3
import json
import requests

banco = accounts[0]
base_URI = "https://ipfs.dweb.link/"

path = "./scripts/filedir/indices.json"

f = open(path, "r")
ipfs_uri = json.load(f)
f.close()


def deploy_contract():
    erc721 = DiceNFT.deploy({"from": banco})
    return erc721


def check_deployedERC721():
    # Check if there is already a deployed contract for the ERC721 token DiceNFT
    if not DiceNFT:
        contract = deploy_contract()
    else:
        contract = DiceNFT[-1]
    return contract

def mint_nftgame(contract):
    # function that mint nft in storage on ipfs
    for i in range(len(ipfs_uri)+1):
        id_index = ipfs_uri[f'{i+1}']
        print(id_index)
        token_uri= f"https://{id_index}.ipfs.dweb.link/"
        print(f'Your token_uri is: {token_uri}')
        contract.createDice(f"DiceToken{i}",token_uri, {"from": banco})
        
    

## Add check mintedNft
     

def main():

    contract = check_deployedERC721()
    mint_nftgame(contract)
