// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.6.0;
pragma experimental ABIEncoderV2;
/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 
 */
   struct Person {
    uint256 number;
    string name;
    }
contract Storage {

    uint256 number;
    
  
    Person[]  people;
    mapping (string => uint256)  nameToPerson;


    /**
     * @dev Store value in variable
     * @param num value to store
     */
    function store(uint256 num ,string memory name) public {
        people.push(Person(num , name));
        nameToPerson[name] = num ;
        ++number;
    }

    /**
     * @dev Return value 
     * @return value of 'number'
     */
       function getByName(string memory name) public view returns (uint256){
        return nameToPerson[name];
    }
   
    function getAll() public view returns ( Person[] memory){
        return people;
    }
     function getNumber() public view returns ( uint256){
        return number;
    }
}