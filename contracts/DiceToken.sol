// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract DiceToken is ERC20 {
    struct Rank {
        address userAddress;
        uint256 points;
        uint256 rank;
    }

    Rank[] public Ranking;

    constructor(uint256 initialSupply) ERC20("DiceToken", "DCT") {
        _mint(msg.sender, initialSupply);
    }

    function setRank(Rank[] memory _data) public {
        delete Ranking;
        for (uint256 i = 0; i < _data.length; i++) {
            Rank memory d = _data[i];
            Rank memory newUser = Rank(d.userAddress, d.points, d.rank);
            Ranking.push(newUser);
        }
    }

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

    function getRank() public view returns (Rank[] memory) {
        return Ranking;
    }
}
