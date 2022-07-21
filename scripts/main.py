from brownie import Contract, accounts
from web3 import Web3
from scripts import deployERC20, deployERC721
from scripts import game

banco = accounts[0]
n_players = int(input("players:"))


def main():


    token = deployERC20.check_deployedERC20()
     
    contract= deployERC721.check_deployedERC721()

    chain_rank = list(token.getRank())



    players = game.game_Set_Up(token, chain_rank, n_players)

    game_players = game.pay_table(players, token)



    game.play(game_players, token, chain_rank,contract)

    deployERC721.buy(token, contract, game_players)
