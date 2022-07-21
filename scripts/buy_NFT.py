from brownie import Contract, DiceNFT,DiceToken,accounts
from web3 import Web3
import random
from scripts import deployERC20
from scripts import deployERC721
from scripts import Player
import json
import urllib.request


banco = accounts[0]
base_URI = "https://dweb.link/ipfs/"
# TODO: rendere questo indipendente dall'ambiente locale
path = "./scripts/filedir/indices.json"

f = open(path, "r")
ipfs_uri = json.load(f)
f.close()

n_players = int(input("players:"))
players = []


def chose_uri(choice, ipfs_uri):
    if (choice==1):
            return ipfs_uri["1"]
    if (choice==2):
            return ipfs_uri["2"]
    if (choice==3):
            return ipfs_uri["3"]
    if (choice==4):
            return ipfs_uri["4"]


def buy(token, contract, players, ipfs_uri):
    buy_players=[]
    for p in players:
        #faccio check sui token, ne deve avere almeno 500
        if token.balanceOf(p.address) >= 500:
            buy_players.append(p)

    for p in buy_players:
        condition = False
        while condition == False:
            response = input(f'player{p.id}:vuoi comprare un NFT per 500 gameToken? y/n ')
            if response == 'y':
                #faccio transfer di quei token e scelgo a caso uri e faccio un createDice
                token.transfer(banco, 500, {"from": p.address})
                choice = random.randint(1, 4)
                cid = chose_uri(choice, ipfs_uri)
                name=input(f'player{p.id}: scegli nome del tuo NFT: ')
                contract.createDice(name, base_URI + cid, {"from": p.address})
                #print(contract.getOwnerDices(p.address))
                condition = True
            elif response == 'n':
                print('ok prossimo giocatore')
                condition = True
            else:
                print('devi specificare y/n')

    
    




        


def main():
    contract = deployERC721.check_deployedERC721()
    token = deployERC20.check_deployedERC20()
    for i in range(n_players):
        players.append(Player.Player(accounts[i + 1], i + 1))
    
    buy(token,contract,players,ipfs_uri)

