# Security Camera with Blockchain Integration

## Project Overview

This project is a security camera system enhanced with blockchain technology. It offers robust security, data integrity, transparency, and decentralized storage for recorded footage. The key blockchain features implemented include timestamping, immutable record-keeping, decentralized storage, and the use of smart contracts to govern system interactions.

## Features

- **Video Capture:** Access the webcam to capture video footage.
- **Face Detection:** Utilize a Haar Cascade classifier to detect faces in the video stream.
- **Continuous Recording:** Automatically record video when a face is detected.
- **Data Integrity:** Implement blockchain timestamping to ensure the recorded data's integrity.
- **Decentralized Storage:** Store recorded footage in a decentralized file storage system (e.g., IPFS).
- **Smart Contracts:** Use smart contracts to govern system interactions, access permissions, and more.

## Getting Started

Follow these steps to set up and run the project on your local machine:

1. **Install Dependencies:** Make sure you have Python and the necessary libraries (OpenCV) installed.

2. **Clone the Repository:** Use `git clone` to obtain the project source code.

3. **Run the Application:** Execute the main Python script to start the security camera system.

## Implementation Details

### Timestamping and Immutable Recordkeeping

- Blockchain technology is used to timestamp each captured video frame, ensuring data integrity.
- Immutable records are stored on the blockchain, making it tamper-proof.

### Decentralized Storage

- The actual video footage is stored in a decentralized file storage system, such as IPFS.
- This decentralized approach increases resilience to network failures and attacks.

### Smart Contracts

- Smart contracts are employed to manage interactions within the security camera system.
- They define rules for adding new footage, verifying data integrity, and managing access permissions.
- Only authorized cameras can add new footage, enhancing system security.

## Contributing

We welcome contributions to this project. Feel free to open issues, suggest improvements, or submit pull requests.


## Acknowledgments

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library.
- [IPFS](https://ipfs.io/): InterPlanetary File System for decentralized storage.

## Author

- [Sanjeev Varma]
- [sanjeevvarmacode@gmail.com]

Thank you for using our Security Camera with Blockchain Integration!

