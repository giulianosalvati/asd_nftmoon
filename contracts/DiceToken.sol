// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract DiceToken is ERC20 {
    //Rank structure
    struct Rank {
        address userAddress;
        uint256 points;
        uint256 rank;
    }

    //Array that contains the global ranking
    Rank[] public Ranking;

    constructor(uint256 initialSupply) ERC20("DiceToken", "DCT") {
        _mint(msg.sender, initialSupply);
    }

    //Update the rank with the points the users won with the last game
    function setRank(Rank[] memory _data) public {
        delete Ranking;
        for (uint256 i = 0; i < _data.length; i++) {
            Rank memory d = _data[i];
            Rank memory newUser = Rank(d.userAddress, d.points, d.rank);
            Ranking.push(newUser);
        }
    }

    //The table pays all the new users
    function welcomeBonus(address[] memory _users, uint256 amount) public {
        for (uint256 i = 0; i < _users.length; i++) {
            transfer(_users[i], amount);
        }
    }

    //Retrieve from the global ranking the _user points
    function getUserPoints(address _user)
        public
        view
        returns (uint256 _points)
    {
        for (uint256 i = 0; i < Ranking.length; i++) {
            if (Ranking[i].userAddress == _user) {
                return Ranking[i].points;
            }
        }
        return 0;
    }

    //Retrieve the rank alltogether
    function getRank() public view returns (Rank[] memory) {
        return Ranking;
    }
}
