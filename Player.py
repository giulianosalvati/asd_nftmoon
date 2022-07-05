class Player:
        
    """
    
    Class Player che prende le cartelle assegnatele dal banco, controlla 
    su di essa i numeri estratti e comunica la vincita.
        Attributi della classe:
            - address: identificativo del giocatore.
            - balanceERC20: numero delle cartelle richieste dal giocatore.
            - cartelle: lista inizializzata vuota che successivamente verrà riempita nel momento in cui 
                       il banco assegna le cartelle richieste dal giocatore.
    
    """
 
    # Costruttore
    def __init__(self , address , NFT= False):
      self.address = address
      self.NFT= NFT
      self.cube= [1,2,3,4,5,6]
      self.score= 0
    
    
    