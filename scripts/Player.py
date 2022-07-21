import random
from unittest import result
from urllib import response
import requests
from scripts import deployERC721
from brownie import accounts 

class Player:

    """

    Class Player
        Attributes:
            - address: player's address
            - id: player's game ID
            - NFT: player's NFT collection
            - dice: The dice from which the game will extract
            - points: player's overall score
            - multi_score: 
            - game_score: Player's game score

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


    def Check_NFT(self, contract):
      """ 
      
      Function do a check on Player NFT balanceOf  
      Parameter: 
          - DiceNFT Contract

      """

      if contract.balanceOf(self.address) >=1:
        self.NFT==True
        token_uri = contract.getOwnerDices(self.address)[0][2]
        response=requests.get(token_uri)
        metadata_uri=response.json()
        self.dice= metadata_uri['value']
        self.multi_score= metadata_uri['score']
        print(f' Player{self.id} is playing with an NFT ')
      
      else:
        print(f"Player{self.id} doesn't have an NFT")


    def extraction(self,contract):
      """
      
      Player makes his throws
      
      Parameter: 
          - DiceNFT Contract
      Return:
          - Player game score
      
      """
      
      self.Check_NFT(contract)
      ex = random.choice(self.dice)
      self.game_score = ex*self.multi_score
      return self.game_score