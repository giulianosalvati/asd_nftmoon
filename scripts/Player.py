import random
from unittest import result
import requests

class Player:
        
    """
    
    Class Player 
        Attributi della classe:
            - address: indirizzo del giocatore.
    
    """
 
    # Costruttore
    def __init__(self , address , id, NFT= False):
      self.address = address
      self.id=id
      self.NFT = NFT
      self.dice = [1,2,3,4,5,6]
      self.score = 0

    def extraction(self):
        return random.choice(self.dice)

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


     

    
    
    