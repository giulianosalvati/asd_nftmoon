from brownie import Contract, DiceNFT, accounts
from web3 import Web3
import json
import random
# import urllib.request
import requests

banco = accounts[0]
base_URI = "https://ipfs.dweb.link/"


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


def chose_uri(choice, ipfs_uri):
    if (choice==1):
            return ipfs_uri["1"]
    if (choice==2):   
            return ipfs_uri["2"]
    if (choice==3):
            return ipfs_uri["3"]
    if (choice==4):
            return ipfs_uri["4"]
    if (choice==5):
            return ipfs_uri["5"]


def main():
    contract = check_deployedERC721()


    # # TODO: rendere questo indipendente dall'ambiente locale
    path = "./scripts/filedir/indices.json"

    f = open(path, "r")
    ipfs_uri = json.load(f)
    f.close()
    
    choice = random.randint(1, 5)
    cid = chose_uri(choice, ipfs_uri)
    print(cid)
    
    token_uri= f"https://{cid}.ipfs.dweb.link/"
    print(token_uri)
    contract.createDice("Ciao",token_uri, {"from": banco})

    # choice = random.randint(1, 4)
    # print(cid)
    # contract.createDice("Bello", base_URI + cid, {"from": banco})
    # print(contract.tokenURI(0))
    
    response= requests.get(token_uri)
    metadata_uri= response.json() # file json
    print(metadata_uri['image'])


    # with urllib.request.urlopen(contract.tokenURI(6)) as url:
    #     data = json.loads(url.read())
    #     print(data["value"])
   
   
   
    # # print(contract.getDices())
    # # print(contract.getOwnerDices(banco))

    # # print(contract.tokenURI(25))