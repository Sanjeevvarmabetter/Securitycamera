// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;


contract Surveillance {
    struct record {
        //hash
        //timestamp
        string ipfshash;
        uint256 timestamp;
    }

    // hash map address to array of records
    mapping(address => record[]) public records;

    // add records

    function addrecord(string memory ipfshash,uint256 timestamp) public {
        //push in to the array with the addresss

        records[msg.sender].push(record(ipfshash,timestamp));
    } 



    //get records

    function getrecord(address user) public view returns(record[] memory) {
        return records[user];
    }

}
