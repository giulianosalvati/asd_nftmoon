from brownie import accounts, Wei
from scripts import Player, Utils
import operator
import time
from web3 import Web3


table = accounts[0]
GAME_PRICE = 10
WELCOME_BONUS = 100


def buy_DCT(player, token, i):
    """

    Function that handles a player with no DCT to play. He can choose to buy DCT with ETH

    """
    print(
        f"\nWelcome back {player.address}. You have no DCT left to play and the game is starting soon. You have the chance to buy some DCT for ETH"
    )

    valid = False
    while not valid:
        choice = input(
            "\nDo you want to buy some DCT. The change is 1 ETH -> 100 DCT y/n "
        )
        if choice == "y":
            amount = int(
                input(
                    f"\nYou have {player.address.balance()/10**18} ETH. How many do you want to spend? "
                )
            )
            if amount <= player.address.balance():
                player.address.transfer(table, amount * 10**18)
                token.transfer(player.address, amount * 100, {"from": table})
                print(
                    f"\nYou now have {token.balanceOf(player.address)} DCT. You will play as Player {i + 1}"
                )
                valid = True
            else:
                print(
                    "\nYou have insufficient balance!! Recharge and be ready for next game"
                )
                valid = True
        elif choice == "n":
            print(
                "\nYou will miss this game!! Recharge and be ready for next game so you don't miss it"
            )
            valid = True
        else:
            print("\nYou have to choose between y (for yes) and n (for no)")


def game_Set_Up(token, chain_rank, n_players):
    """

    Function that sets the Game up and creates the list of players

    """
    players = []
    new_players = []
    for i in range(n_players):

        address = accounts[i + 1]
        points = token.getUserPoints(address)
        player = Player.Player(address, i + 1, points)

        # If the player never logged in he can receive the welcome bonus
        if (
            not Utils.check_If_Player_In_Blockcahin_Rank(address, chain_rank)
            and token.balanceOf(player.address) == 0
        ):
            print(
                f"\nWelcome {player.address}. You get a welcome Bonus of 100 DCT. You can start playing the game. Your ID for the current game is {i+1}\n"
            )
            new_players.append(player.address)
            players.append(player)
        elif token.balanceOf(player.address) == 0:
            buy_DCT(player, token, i)
            players.append(player)
        else:
            print(
                f"\nAdded {player.address} as Player {player.id} overall points = {player.points}. You have {token.balanceOf(player.address)} DCT left\n"
            )
            players.append(player)
    if len(new_players) > 0:
        token.welcomeBonus(new_players, WELCOME_BONUS, {"from": table})
    return players


def pay_table(players, token):
    """

    Function that pays the table before starting the game

    """
    print("\n\nAll players will now pay the table and the game will begin!!!\n\n")
    game_players = []
    addresses = []
    for p in players:
        if token.balanceOf(p.address) >= GAME_PRICE:
            token.transfer(table, GAME_PRICE, {"from": p.address})
            game_players.append(p)
            addresses.append(p.address)
    return game_players


def create_Game_Rank(game_players, contract):
    """

    Function that creates a game rank based on the points obtained by the players during the current game

    """
    scores = []
    for p in game_players:
        p_score = p.extraction(contract)
        print(f"\nPlayer {p.id} score is: {p_score}")
        if p.multiplier != 1:
            print(f"With your NFT multiplier your score went up to: {p.game_score}\n")
        scores.append([p.game_score, p])
    scores.sort(key=operator.itemgetter(0), reverse=True)
    return scores


def pay_Winners(scores, token):
    """

    Function that awards the winners of the current game

    """
    print("\n\nThe table will now pay the winners. Congratulations !!\n\n")

    winner = scores[0][1]  # The winner gets 50 token
    second = scores[1][1]  # The runner-up gets 30 token
    third = scores[2][1]  # The third best gets 20 token

    # Pay winners
    token.transfer(winner.address, 50, {"from": table})
    token.transfer(second.address, 30, {"from": table})
    token.transfer(third.address, 20, {"from": table})

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
    """

    Function that updates the blockchain ranking based on the points obtained during the current game

    """
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

    # Update the rank field and put everithing into the final rank
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


def play(game_players, token, chain_rank, contract):
    """

    Function that handles all aspects of the game

    """

    scores = create_Game_Rank(game_players, contract)

    winners = pay_Winners(scores, token)

    update_Chain_Ranking(winners, chain_rank, token)
