from brownie import Contract, DiceNFT, accounts
from web3 import Web3
import json
import random


banco = accounts[0]
base_URI = "http://localhost:8080/ipfs/"


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
        case 5:
            return ipfs_uri["5"]


def main():
    contract = check_deployedERC721()

    # TODO: rendere questo indipendente dall'ambiente locale
    path = "C:/Users/massi/OneDrive/Desktop/Campus/Architetture di Sistemi Distribuiti/NFT/asd_nftmoon/scripts/filedir/indices.json"

    f = open(path, "r")
    ipfs_uri = json.load(f)
    f.close()

    choice = random.randint(1, 5)
    ipfs = chose_uri(choice, ipfs_uri)
    print(ipfs)
    contract.createDice("Dice1", base_URI + ipfs, {"from": banco})
    print(contract.tokenURI(0))
    choice = random.randint(1, 5)
    print(ipfs)
    contract.createDice("Dice1", base_URI + ipfs, {"from": banco})

    # print(contract.getDices())
    # print(contract.getOwnerDices(banco))

    print(contract.tokenURI(1))
