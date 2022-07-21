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
    if (choice==1):
            return ipfs_uri["1"]
    if (choice==2):
            return ipfs_uri["2"]
    if (choice==3):
            return ipfs_uri["3"]
    if (choice==4):
            return ipfs_uri["4"]

def buy(token, contract, players):
    buy_players=[]
    for p in players:
        #faccio check sui token, ne deve avere almeno 500
        if token.balanceOf(p.address) >= 500:
            buy_players.append(p)

    for p in buy_players:
        condition = False
        while not condition:
            response = input(f'player{p.id}:vuoi comprare un NFT? y/n ')
            if response == 'y':
                listDices=contract.getOwnerDices(banco)
                listNFT=[]
                for j in listDices:
                    listNFT.append(listDices[j][1])
                choice = input(f'player{p.id}: quale NFT vuoi comprare tra i disponibili?{listNFT}')
                token.transfer(banco, 500, {"from": p.address})
                contract.transferFrom(banco, p.address, choice, {"from": banco})
                #print(contract.getOwnerDices(p.address))
                condition = True
            elif response == 'n':
                print('ok prossimo giocatore')
                condition = True
            else:
                print('devi specificare y/n')

def main():
    contract = check_deployedERC721()

    # TODO: rendere questo indipendente dall'ambiente locale
    path = "./scripts/filedir/indices.json"

    f = open(path, "r")
    ipfs_uri = json.load(f)
    f.close()

    choice = random.randint(1, 4)
    cid = chose_uri(choice, ipfs_uri)
    print(cid)
    contract.createDice("Ciao", base_URI + cid, {"from": banco})
    print(base_URI + cid)
    print(f"\n\n\n{contract.tokenURI(6)}")
    choice = random.randint(1, 4)
    print(cid)
    contract.createDice("Bello", base_URI + cid, {"from": banco})
    print(f"\n\n\n{contract.tokenURI(7)}")
    print(contract.tokenURI(7))
    with urllib.request.urlopen(contract.tokenURI(6)) as url:
        data = json.loads(url.read())
        print(data["value"])
    # print(contract.getDices())
    # print(contract.getOwnerDices(banco))

    # print(contract.tokenURI(25))
