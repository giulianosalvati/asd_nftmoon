// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract DiceNFT is ERC721URIStorage, Ownable {
    uint256 COUNTER;

    constructor() ERC721("DiceNFT", "DNFT") {
        COUNTER = 0;
    }

    //Struttura per la carta. da rivedere?!?!
    struct Dice {
        string name;
        uint256 id;
        string uri;
    }

    //array dove vengono salvati gli nft creati
    Dice[] public Dices;
    mapping(address => Dice[]) public dices;

    //Mi serve gestire l'evento che la funzione emit del mint lancia(come transazione)
    event NewDice(address indexed owner, uint256 id, string uri);

    //Creation of the NFT
    function createDice(string memory _name, string calldata _uri)
        public
        returns (uint256)
    {
        Dice memory newDice = Dice(_name, COUNTER, _uri);
        Dices.push(newDice);
        _safeMint(msg.sender, COUNTER);
        _setTokenURI(COUNTER, _uri);
        emit NewDice(msg.sender, COUNTER, _uri);
        COUNTER++;
        return COUNTER - 1;
    }

    //Per riuscire a prendere la lista di Nft
    function getDices() public view returns (Dice[] memory) {
        return Dices;
    }

    //Per prendere solo gli nft dell'owner
    function getOwnerDices(address _user) public view returns (Dice[] memory) {
        Dice[] memory result = new Dice[](balanceOf(_user));
        uint256 counter = 0;
        for (uint256 i = 0; i < Dices.length; i++) {
            if (_user == ownerOf(i)) {
                result[counter] = Dices[i];
                counter++;
            }
        }
        return result;
    }
}
