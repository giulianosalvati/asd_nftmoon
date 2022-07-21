import random
from unittest import result
from urllib import response
import requests
from scripts import deployERC721
from brownie import accounts 

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
        self.dice = range(1,51)
        self.multi_score= 1
        self.game_score = 0


    # #check if the player is an NFT owner
    # def Check_NFT(self, contract):
    #   if contract.balanceOf(self.address) >=1:
    #     self.NFT==True
    #     #token URI
    #     result = contract.getOwnerDices(self.address)[0][2]
    #     return result
      
    #   else:
    #     pass

    #update normal dices with NFT values     
    def Check_NFT(self, contract):
      if contract.balanceOf(self.address) >=1:
        self.NFT==True
        #token URI
        uri = contract.getOwnerDices(self.address)[0][2]
        response=requests.get(uri)
        metadata_uri=response.json()
        self.dice=metadata_uri['value']
        self.multi_score=metadata_uri['score']
        print('NFT convalidato')
      
      else:
        print('Player no NFT')


    def extraction(self,contract):
        self.Check_NFT(contract)
        ex = random.choice(self.dice)
        self.game_score = ex*self.multi_score
        return ex

