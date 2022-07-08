from brownie import Contract, accounts
from web3 import Web3
import random
from scripts import Player


banco=accounts[0]

def play(players,token,n_players):
    results=[]
    for p in players:
        results.append(p.extraction())
    
    score = results[:]
    score.sort(reverse=True)
    print(results)
    
    for p in players:
        print(f'player{p.id}:{token.balanceOf(p.address)}')

    first = results.index(score[0])  # The winner gets 50 token
    token.transfer(players[first].address, 50, {"from": banco})

    second = results.index(score[1])  # The runner-up gets 30 token
    token.transfer(players[second].address, 30, {"from": banco})

    third = results.index(score[2]) # The third best gets 20 token
    token.transfer(players[third].address, 20, {"from": banco})

    for p in players:
        print(f'player{p.id}:{token.balanceOf(p.address)}')
    

def initial_transaction(players,token):
    for p in players:
        print(f'player{p.id}:{token.balanceOf(p.address)}')
        token.transfer(p.address, 100, {"from": banco})  # do 100 token ad ogni giocatore
        print(f'player{p.id}:{token.balanceOf(p.address)}')
    
def check_token(players,token):
    play_players=[]
    for p in players:
        if(token.balanceOf(p.address)>=10):
            token.transfer(banco, 10, {"from":p.address})
            play_players.append(p)
    
    return play_players
            

