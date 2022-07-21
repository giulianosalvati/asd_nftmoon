import random
from unittest import result
import requests


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


    #check if the player is an NFT owner
    def Check_NFT(self, contract):
      if contract.balanceOf(self.address) >=1:
        self.NFT==True
        #token URI
        result = contract.getDices(self.address)[0][2]
        return result

      else:
        pass

    #update normal dices with NFT values     
    def update_Dice_values(self, contract):
      uri = self.Check_NFT(contract)
      values=requests.get(uri)
      self.dice=values['values']
      self.score=values['score']


    def extraction(self):
        ex = random.choice(self.dice)
        self.game_score = ex
        return ex

