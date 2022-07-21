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
    """
    
     DiceNFT contract deploys
    
    """

    erc721 = DiceNFT.deploy({"from": banco})
    return erc721


def check_deployedERC721():
    '''
    Check if there is already a deployed contract for the ERC721 token DiceNFT
    '''
    if not DiceNFT:
        contract = deploy_contract()
        mint_nftgame(contract)
    else:
        contract = DiceNFT[-1]
    return contract

def mint_nftgame(contract):
    '''
    Function that mints DiceToken NFTs in storage on Ipfs
    '''
    for i in range(len(ipfs_uri)):
        id_index = ipfs_uri[f'{i+1}']
        token_uri= f"https://{id_index}.ipfs.dweb.link/"
        print(f'Token_uri minted: {token_uri}')
        contract.createDice(f"DiceToken{i+1}",token_uri, {"from": banco})
    


def buy(token, contract, players):
    '''
    Function that allows to buy NFT ( Only for player with almost 80 DCT and with a balanceOf = 0) at the end of the game.
    '''
    buy_players=[]
    for p in players:
        # check on DCT balance, it pass with almost 80
        if token.balanceOf(p.address) >= 80 and contract.balanceOf(p.address)< 1:
            buy_players.append(p)

    for p in buy_players:
        condition = False
        while not condition:
            response = input(f'Player{p.id}: Would you like to buy an NFT? y/n ')
            if response == 'y':
                listDices=contract.getOwnerDices(banco)
                listNFT=[]
                for j in range(0,len(listDices)):
                    listNFT.append(listDices[j][1])
                choice = input(f'player{p.id}: Which available NFT do you want to buy?{listNFT} ')
                token.transfer(banco, 80, {"from": p.address})
                contract.transferFrom(banco, p.address, choice, {"from": banco})
                condition = True
            elif response == 'n':
                print('Ok thanks, next Player ')
                condition = True
            else:
                print(' You have to specify y/n')