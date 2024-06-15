const { ethers } = require("hardhat");

async function main() {
    try {
        const [deployer] = await ethers.getSigners();
        const Surveillance = await ethers.getContractFactory("Surveillance");
        const surveillance = await Surveillance.attach("0xE2A8C7006686A9C4317692bDE46e410192bacAb1");

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
