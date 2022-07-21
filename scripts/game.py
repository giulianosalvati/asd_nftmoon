from brownie import Contract, accounts
from web3 import Web3
import random
from scripts import Player, Utils
import operator
import time


table = accounts[0]

# Welcome bonus for first time users only
def welcome_bonus(player, token, i):
    if token.balanceOf(player.address) == 0:
        print(
            f"\nWelcome {player.address}. You get a welcome Bonus of 100 DCT. You can start playing the game. Your ID for the current game is {i+1}\n"
        )
        token.transfer(player.address, 100, {"from": table})
    else:
        print(
            f"Added {player.address} as {player.id} overall points = {player.points}. You have {token.balanceOf(player.address)} DCT left\n"
        )


# Creates the player list for the game. If the player is new he recives a welcome bonus and gets added to the blockchain
def game_Set_Up(token, chain_rank, n_players):
    players = []
    for i in range(n_players):
        address = accounts[i + 1]
        points = token.getUserPoints(address)
        players.append(Player.Player(address, i + 1, points))
        # If the player never logged in he can receive the welcome bonus
        if not Utils.check_If_Player_In_Blockcahin_Rank(address, chain_rank):
            welcome_bonus(players[i], token, i)
        else:
            print(
                f"Added {address} as {players[i].id} overall points = {points}. You have {token.balanceOf(address)} DCT left\n"
            )
    return players


# Check if players have enough DCT tokens to play and pay table. If not discard them
def pay_table(players, token):
    print("\n\nAll players will now pay the table and the game will begin!!!\n\n")
    game_players = []
    for p in players:
        if token.balanceOf(p.address) >= 10:
            token.transfer(table, 10, {"from": p.address})
            game_players.append(p)
    return game_players


# For every playing player extract a value from its dice and create a sorted score board with extraction values and related player object
def create_Game_Rank(game_players,contract):
    scores = []
    for p in game_players:
        p_score = [p.extraction(contract), p]
        scores.append(p_score)
        print(f"\nPlayer {p.id} game_score is: {p.game_score}")
    scores.sort(key=operator.itemgetter(0), reverse=True)
    return scores


# Pay winners, update player points and create the winner list to be merged into the Chain ranking
def pay_Winners(scores, token):
    print("\n\nThe table will now pay the winners. Congratulations !!\n\n")

    winner = scores[0][1]  # The winner gets 50 token
    second = scores[1][1]  # The runner-up gets 30 token
    third = scores[2][1]  # The third best gets 20 token

    # Pay winners
    token.transfer(winner.address, 50, {"from": table})
    token.transfer(second.address, 30, {"from": table})
    token.transfer(third.address, 30, {"from": table})

    # Update players points
    winner.points = winner.points + 50
    second.points = second.points + 30
    third.points = third.points + 20

    # Create list of tuples compatible with the structure of the Chain ranking
    winners = [
        (winner.address, winner.points, 0),
        (second.address, second.points, 0),
        (third.address, third.points, 0),
    ]
    return winners


def update_Chain_Ranking(winners, chain_rank, token):
    print("\n\nUpdating game results to Global DCT Ranking....")
    start = time.time()
    # New ranking
    new_rank = winners
    for c in chain_rank:
        found = False
        for w in winners:
            # If c is an old record of the player it must be ingnored
            if w[0] in c:
                found = True
                break
        if not found:
            new_rank.append(c)

    # Sort the updated chain_rank by points
    new_rank.sort(key=operator.itemgetter(1), reverse=True)

    # Update the rank and put everithing into the final rank
    rank = 1
    final_rank = []
    for n_r in new_rank:
        temp = list(n_r)
        temp[2] = rank
        final_rank.append(tuple(temp))
        print(f"\n{temp[0]} rank is now {temp[2]} with a total of {temp[1]} points")
        rank += 1

    # Push the updated rank to the blockchain
    token.setRank(final_rank, {"from": table})
    finish = time.time()
    print(token.getRank())
    print(f"\n\n...Update completed in {finish-start}s")


def play(game_players, token, chain_rank,contract):

    scores = create_Game_Rank(game_players,contract)

    winners = pay_Winners(scores, token)

    update_Chain_Ranking(winners, chain_rank, token)
