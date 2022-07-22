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

    //DiceNFT structure
    struct Dice {
        string name;
        uint256 id;
        string uri;
    }

    //Array where all the NFTs will be stored
    Dice[] public Dices;

    //The event to emit when a new Dice NFT is created
    event NewDice(address indexed owner, uint256 id, string uri);

    //Mint a new NFT
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

    //Retrieve all Dices
    function getDices() public view returns (Dice[] memory) {
        return Dices;
    }

    //Retrieve all the _user NFTs
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
