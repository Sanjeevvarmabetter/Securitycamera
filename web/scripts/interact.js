const { ethers } = require("hardhat");

async function main() {
    try {
        const [deployer] = await ethers.getSigners();
        const Surveillance = await ethers.getContractFactory("Surveillance");
        const surveillance = awaitw Surveillance.attach("0x83B8fC51546503972c2eBdea2d7ddD7179F3F1f6");

        // Add a record
        await surveillance.addrecord("testHash", 1623864723);
        console.log("Record added successfully.");

        // Get records
        const records = await surveillance.getrecord(deployer.address);
        console.log("Retrieved records:", records);
    } catch (error) {
        console.error("Error:", error);
    }
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Script execution error:", error);
        process.exit(1);
    });
