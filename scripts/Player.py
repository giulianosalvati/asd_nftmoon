import random

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

    
    
    