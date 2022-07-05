from brownie import Contract, ERC20Basic,accounts
from web3 import Web3
import random

banco=accounts[0]
giocatore1=accounts[1]
giocatore2=accounts[2]
giocatore3=accounts[3]

data={
    "address":[accounts[1],accounts[2],accounts[3]],
    "balance":[],
    "points":[]
}



def deploy_token():
    erc20=ERC20Basic.deploy({"from": banco})
    return erc20

def extraction():
    return random.randint(1,6)

def initial_transaction(token):
    for i in range(len(data["address"])):
        token.transfer(data["address"][i], 1000, {"from": banco}) # do 1000 token ad ogni giocatore
        data["balance"].append(token.balanceOf(data["address"][i])) #aggiorno i balance
    return

def update_balance(token):
    if len(data["balance"])==0:
        for i in range(len(data["address"])):
            data["balance"].append(token.balanceOf(data["address"][i])) #salvo i balance
    else:
        for i in range(len(data["address"])):   
            data["balance"][i]=(token.balanceOf(data["address"][i])) #aggiorno i balance


def main():
    # token=deploy_token()
    token=Contract('0x717bAc92dE6866076574E75ADaB73778A0fEe882')
    #initial_transaction(token)
    update_balance(token)
    print(data["balance"])    

    for i in range(len(data["address"])):
        data["points"].append(extraction())
    
    results=data["points"]
    results.sort(reverse=True)
    first=data["points"].index(results[0]) #trovo vincitore e gli do 50 token
    token.transfer(data["address"][first], 50, {"from": banco})

    second=data["points"].index(results[1]) #trovo secondo e gli do 30 token
    token.transfer(data["address"][second], 30, {"from": banco})

    third=data["points"].index(results[2]) #trovo terzo e gli do 20 token
    token.transfer(data["address"][third], 20, {"from": banco})
    
    update_balance(token)
    print(data["points"]) 
    print(data["balance"])
    
    