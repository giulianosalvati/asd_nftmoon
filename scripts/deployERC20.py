from brownie import Contract, DiceToken, accounts
from web3 import Web3
import random

banco = accounts[0]
initialSupply = 10**26  # 1M tokens


def deploy_token():
    erc20 = DiceToken.deploy(initialSupply, {"from": banco})
    return erc20

def check_deployedERC20():
    # Check if there is already a deployed contract for the ERC20 token DiceToken
    if not DiceToken:
        token = deploy_token()
    else:
        token = DiceToken[-1]
    return token
