import random


class Player:

    """

    Class Player
        Attributi della classe:
            - address: player's address
            - id: player's game ID
            - NFT: player's NFT collection
            - dice: The dice from which the game will extract
            - points: player's overall score

    """

    # Constructor
    def __init__(self, address, id, points, NFT=False):
        self.address = address
        self.id = id
        self.points = points
        self.NFT = NFT
        self.dice = range(1, 100)
        self.game_score = 0

    def extraction(self):
        ex = random.choice(self.dice)
        self.game_score = ex
        return ex
