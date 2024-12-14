// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

contract newContract {
    uint public StudentId;
    address public owner;

    constructor() {
        StudentId = 10; // Initial StudentId
        owner = msg.sender; // Set the deployer as the owner
    }

    function viewMyId() public view returns(uint) {
        return StudentId;
    }

    function updateID(uint _newId) public {
        require(msg.sender == owner, "Only the owner can update the ID");
        StudentId = _newId;
    }
}
