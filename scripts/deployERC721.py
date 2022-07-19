from brownie import Contract, DiceNFT, accounts
from web3 import Web3
import json
import random
import urllib.request


banco = accounts[0]
base_URI = "https://dweb.link/ipfs/"


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
    match choice:
        case 1:
            return ipfs_uri["1"]
        case 2:
            return ipfs_uri["2"]
        case 3:
            return ipfs_uri["3"]
        case 4:
            return ipfs_uri["4"]


def main():
    contract = check_deployedERC721()

    # TODO: rendere questo indipendente dall'ambiente locale
    path = "./scripts/filedir/indices.json"

    f = open(path, "r")
    ipfs_uri = json.load(f)
    f.close()

    """ choice = random.randint(1, 4)
    cid = chose_uri(choice, ipfs_uri)
    print(cid)
    contract.createDice("Ciao", base_URI + cid, {"from": banco})
    print(base_URI + cid)
    print(f"\n\n\n{contract.tokenURI(25)}")
    choice = random.randint(1, 4)
    print(cid)
    contract.createDice("Bello", base_URI + cid, {"from": banco})
    print(f"\n\n\n{contract.tokenURI(26)}") """
    print(contract.tokenURI(0))
    with urllib.request.urlopen(contract.tokenURI(0)) as url:
        data = json.loads(url.read())
        print(data["value"])
    # print(contract.getDices())
    # print(contract.getOwnerDices(banco))

    # print(contract.tokenURI(25))
