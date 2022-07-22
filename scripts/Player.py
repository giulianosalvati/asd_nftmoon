import random
import requests


class Player:

    """

    Class Player
        Attributes:
            - address: player's address
            - id: player's game ID
            - NFT: player's NFT collection
            - dice: The dice from which the game will extract
            - points: player's overall score
            - multiplier:
            - game_score: Player's game score

    """

    # Constructor
    def __init__(self, address, id, points, NFT=None):
        self.address = address
        self.id = id
        self.points = points
        self.NFT = NFT
        self.dice = range(1, 51)
        self.multiplier = 1
        self.game_score = 0

    def Check_NFT(self, erc721):
        """

        Function that checks if the Player has an NFT in his balance.
        If yes set the NFT attribute with the NFT metadata and give the NFT multiplier and dice to the player.

        """
        if erc721.balanceOf(self.address) >= 1:
            dice = erc721.getOwnerDices(self.address)[0]
            print(f"\nPlayer {self.id} is playing with the NFT {dice[0]}")
            token_uri = dice[2]
            response = requests.get(token_uri)
            nft_metadata = response.json()
            self.NFT = nft_metadata
            self.dice = nft_metadata["value"]
            self.multiplier = nft_metadata["score"]

        else:
            print(f"\nPlayer{self.id} doesn't have an NFT")

    def extraction(self, erc721):
        """

        Player makes his throw. The game score gets updated.
        Return the value of the extraction with no NFT multiplier applied

        """

        self.Check_NFT(erc721)
        ex = random.choice(self.dice)
        self.game_score = ex * self.multiplier
        return ex
