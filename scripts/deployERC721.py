from brownie import Contract, DiceNFT, accounts
from web3 import Web3


banco = accounts[0]


def deploy_contract():
    erc721 = DiceNFT.deploy({"from": banco})
    return erc721


def check_deployedERC721():
    # Check if there is already a deployed contract for the ERC721 token DiceNFT
    if not DiceNFT:
        contract = deploy_contract()
    else:
        contract = DiceNFT[-1]
    return contract


def main():
    contract = check_deployedERC721()
    contract._createDice("Dice1", {"from": banco})
    contract._createDice("Dice2", {"from": banco})
    contract._createDice("Dice3", {"from": banco})
    contract._createDice("Dice4", {"from": banco})
    print(contract.getDices())
    print(contract.getOwnerDices(banco))
