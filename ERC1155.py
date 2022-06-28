from brownie import NftToken,accounts
from web3 import Web3
import random

uri ="https://bafybeiagpv36lbtriaxpq3awkhdkep6ixcjivyhz4k3rqaznjwy27fedsy.ipfs.dweb.link/{id}.json"
price=10
banco=accounts[0]
giocatore=accounts[1]


def deploy_token():
    erc1155token=NftToken.deploy({"from": banco})
    return erc1155token

def extraction():
    return random.randint(1,6)

def play(contract,banco,giocatore):
    b=extraction()
    g=extraction()
    if(b>=g):
        print("vince banco")
    else:
        print("vince giocatore")
        contract.safeTransferFrom(banco,giocatore,1,2*price,'0x0',{"from":banco})
        

def app(contract,banco,giocatore):
    #giocatore ha già i token
    condition= 'y'
    while condition== 'y':
        if(contract.balanceOf(giocatore, 1)>=price):
            print("puoi giocare")
            contract.safeTransferFrom(giocatore,banco,1,10,'0x0',{"from":giocatore})
            print(contract.balanceOf(giocatore,1))
            play(contract,banco,giocatore)
            print(contract.balanceOf(giocatore,1))   
        else:
            pay_banco(contract,banco,giocatore)

        condition = input("Vuoi continuare? y/n")


def pay_banco(contract,banco,giocatore):
    if(giocatore.balance()>=10**18):
        print(giocatore.balance())
        giocatore.transfer(to=banco,amount=10**18)
        print(giocatore.balance())
        contract.safeTransferFrom(banco,giocatore,1,100,'0x0',{"from":banco})
        print(contract.balanceOf(giocatore,1))
        
    else:
        print("non hai abbastanza soldi")
    



def main():
    token=deploy_token()
    app(token,banco,giocatore)
