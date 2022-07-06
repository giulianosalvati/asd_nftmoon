// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DiceNFT is ERC721, Ownable {
    uint256 COUNTER;

    constructor() ERC721("DiceNFT", "DNFT") {
        COUNTER = 0;
    }

    //Struttura per la carta. da rivedere?!?!
    struct Dice {
        string name;
        uint256 id;
    }

    //array dove vengono salvati gli nft creati
    Dice[] public Dices;

    //Mi serve gestire l'evento che la funzione emit del mint lancia(come transazione)
    event NewDice(address indexed owner, uint256 id);

    //Creation of the NFT
    function _createDice(string memory _name) public returns (uint256) {
        Dice memory newDice = Dice(_name, COUNTER);
        Dices.push(newDice);
        _safeMint(msg.sender, COUNTER);
        emit NewDice(msg.sender, COUNTER);
        COUNTER++;
        return COUNTER - 1;
    }

    //Per riuscire a prendere la lista di Nft
    function getDices() public view returns (Dice[] memory) {
        return Dices;
    }

    //Per prendere solo gli nft dell'owner
    function getOwnerDices(address _owner) public view returns (Dice[] memory) {
        Dice[] memory result = new Dice[](balanceOf(_owner));
        uint256 counter = 0;
        for (uint256 i = 0; i < Dices.length; i++) {
            result[counter] = Dices[i];
            counter++;
        }
        return result;
    }
}
