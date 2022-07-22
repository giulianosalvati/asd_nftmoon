from brownie import DiceNFT, accounts
import json


table = accounts[0]
base_URI = "https://ipfs.dweb.link/"

path = "./scripts/filedir/indices.json"

f = open(path, "r")
ipfs_uri = json.load(f)
f.close()


def deploy_contract():
    """

    DiceNFT contract deploy function

    """
    erc721 = DiceNFT.deploy({"from": table})
    return erc721


def check_deployedERC721():
    """

    Check if there is already a deployed contract for the ERC721 token DiceNFT. If not deploy and mint NFT collection

    """
    if not DiceNFT:
        print("\n\nMinting ERC721 contract for DiceNFT..")
        erc721 = deploy_contract()
        print("...and minting the DiceNFT collection\n\n")
        mint_dice_nfts(erc721)
    else:
        erc721 = DiceNFT[-1]
    return erc721


def mint_dice_nfts(erc721):
    """

    Function that mints DiceNFT NFTs collection stored on Ipfs

    """
    for i in range(len(ipfs_uri)):
        id_index = ipfs_uri[f"{i+1}"]
        token_uri = f"https://{id_index}.ipfs.dweb.link/"
        print(f"\nDiceNFT{i+1} minted with uri: {token_uri}\n")
        erc721.createDice(f"DiceNFT{i+1}", token_uri, {"from": table})


def select_Buy_NFT_players(erc20, erc721, players):
    """

    Function that selects the players who can afford to buy an NFT (150 DCT). If the player has an NFT he is not elegible to buy another

    """
    buy_players = []
    for p in players:
        if erc20.balanceOf(p.address) >= 150 and erc721.balanceOf(p.address) == 0:
            buy_players.append(p)
    return buy_players


def show_Available_NFTs(erc721):
    """
    Function that creates the list of the avilable NFTs to be shown to the players who want to buy one

    """
    available_NFTs = erc721.getOwnerDices(table)
    NFTlist = []
    for j in range(0, len(available_NFTs)):
        NFTlist.append(
            [
                available_NFTs[j][1],
                f"DiceToken{available_NFTs[j][1]}",
                available_NFTs[j][2],
            ]
        )
    return NFTlist


def choose_NFT_From_List(NFTlist, player):
    """

    Print each NFT in a new line

    """
    print(
        f"\n\nPlayer {player.id}, the following list contains the list of the available NFTs. You can CTRL+click to follow each link and see every NFT effect\n\n"
    )
    for nft in NFTlist:
        print(f"\n{nft}")

    valid = False
    while not valid:
        choice = input(
            f"\n So Player {player.id}: Which one of the available NFTs do you want to buy? "
        )
        for nft in NFTlist:
            if choice in nft:
                return choice
        else:
            print("\nPlease choose an NFT from the list of the availables!!")


def buy(erc20, erc721, players):
    """

    Function that allows to buy NFT to players

    """
    buy_players = select_Buy_NFT_players(erc20, erc721, players)

    for p in buy_players:
        condition = False
        while not condition:
            response = input(
                f"\nPlayer {p.id} you have {erc20.balanceOf(p.address)}DCT left: Would you like to buy an NFT? y/n "
            )
            if response == "y":
                NFTlist = show_Available_NFTs(erc721)
                choice = choose_NFT_From_List(NFTlist, p)
                erc20.transfer(table, 150, {"from": p.address})
                erc721.transferFrom(table, p.address, choice, {"from": table})
                condition = True
            elif response == "n":
                print("\nOk no problem. See you next game!!!")
                condition = True
            else:
                print("\nYou have to specify y (for yes) of n (for no)")
