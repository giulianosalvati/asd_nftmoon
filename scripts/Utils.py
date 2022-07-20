# Check if a player is already in the blockchain or not
def check_If_Player_In_Blockcahin_Rank(address, chain_rank):
    for record in chain_rank:
        if address in record:
            return True
    return False
