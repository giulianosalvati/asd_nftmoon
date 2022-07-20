import random
from unittest import result

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

    def Check_NFT(self, contract):
      if contract.balanceOf(self.address) >=1:
        self.NFT==True
        result = contract.getDices(self.address)[0][1]
        return result

      else:
        pass

     

    
    
    