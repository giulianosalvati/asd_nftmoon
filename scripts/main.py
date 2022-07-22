from brownie import accounts
from scripts import deployERC20, deployERC721, game

table = accounts[0]
valid = False
while not valid:
    n_players = int(input("\nChoose the number of players: "))
    if n_players >= 3 and n_players <= len(accounts) - 1:
        valid = True
    else:
        print(f"\nYou need to specify a number between 3 and {len(accounts)-1}")


def main():

    erc20 = deployERC20.check_deployedERC20()

    erc721 = deployERC721.check_deployedERC721()

    chain_rank = list(erc20.getRank())

    players = game.game_Set_Up(erc20, chain_rank, n_players)

    game_players = game.pay_table(players, erc20)

    game.play(game_players, erc20, chain_rank, erc721)

    deployERC721.buy(erc20, erc721, game_players)
