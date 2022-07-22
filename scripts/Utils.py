def check_If_Player_In_Blockcahin_Rank(address, chain_rank):
    """

    Function that checks if a player is already ranked in the blockchain

    """
    for record in chain_rank:
        if address in record:
            return True
    return False
