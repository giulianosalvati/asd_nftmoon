from brownie import Contract, DiceNFT, accounts
from web3 import Web3
import json


banco = accounts[0]
base_URI = "https://ipfs.dweb.link/"

path = "./scripts/filedir/indices.json"

f = open(path, "r")
ipfs_uri = json.load(f)
f.close()


def deploy_contract():
    '''
    check_deployedERC721 check if there is a DiceNFT yet deployed 
    else it deploy it so, from the first game run, we've only one DiceNft contract
    '''
    erc721 = DiceNFT.deploy({"from": banco})
    return erc721


def check_deployedERC721():
    # Check if there is already a deployed contract for the ERC721 token DiceNFT
    if not DiceNFT:
        contract = deploy_contract()
        mint_nftgame(contract)
    else:
        contract = DiceNFT[-1]
    return contract

def mint_nftgame(contract):
    # function that mint nft in storage on ipfs
    for i in range(len(ipfs_uri)):
        id_index = ipfs_uri[f'{i+1}']
        print(id_index)
        token_uri= f"https://{id_index}.ipfs.dweb.link/"
        print(f'Your token_uri is: {token_uri}')
        contract.createDice(f"DiceToken{i+1}",token_uri, {"from": banco})
        

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
