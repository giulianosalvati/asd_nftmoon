from brownie import Contract, accounts
from web3 import Web3
import random
from scripts import deployERC20
from scripts import Player
from scripts import game
from scripts import Utils

banco = accounts[0]
n_players=int(input('players:'))
players=[]


def main():
   
    token=deployERC20.check_deployedERC20()

    
    for i in range(n_players): 
        players.append(Player.Player(accounts[i+1], i+1))
        print(players[i].id)
    
    
    #game.initial_transaction(players,token)
    play_players=game.check_token(players,token)
    game.play(play_players,token,n_players)

    
    
    
    


