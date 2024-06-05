const { ethers } = require("hardhat");

async function main() {
    const [deployer] = await ethers.getSigners(); /// this wil retrive the deployers account
    console.log("Deploying contracts with the account ",deployer);

    const Surveillance  = await ethers.getContractFactory("Surveillance");
    const contract = await Surveillance.deploy();
    
    console.log("Contract deployed to: ",contract);

};

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });


