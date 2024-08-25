import cv2
import datetime
import time
import ipfshttpclient
import os
from web3 import Web3


# Connect to the Ethereum contract
def connect_to_contract():
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

    contract_address = "0xF872B1401C8FAaAd1A66d31Ab369D9E48551cCd3"
    contract_abi = [
        {
            "inputs": [
                {"internalType": "string", "name": "ipfshash", "type": "string"},
                {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
            ],
            "name": "addrecord",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
            "name": "getrecord",
            "outputs": [
                {
                    "components": [
                        {"internalType": "string", "name": "ipfshash", "type": "string"},
                        {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
                    ],
                    "internalType": "struct Surveillance.record[]",
                    "name": "",
                    "type": "tuple[]"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "uint256", "name": "", "type": "uint256"}
            ],
            "name": "records",
            "outputs": [
                {"internalType": "string", "name": "ipfshash", "type": "string"},
                {"internalType": "uint256", "name": "timestamp", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]
    return w3, w3.eth.contract(address=contract_address, abi=contract_abi)


# Record video when a face is detected
def record_video():
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detection = False
    detection_stopped_time = None
    timer_start = False
    delay_seconds = 2

    frame_size = (int(video.get(3)), int(video.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = None

    while True:
        ret, frame = video.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            if detection:
                timer_start = False
            else:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"./record_videos/{current_time}.mp4", fourcc, 20, frame_size)
                print("Started recording!!")

        elif detection:
            if timer_start:
                if time.time() - detection_stopped_time >= delay_seconds:
                    detection = False
                    timer_start = False
                    if out:
                        out.release()
                        print("Stopped recording")
            else:
                timer_start = True
                detection_stopped_time = time.time()

        if detection:
            out.write(frame)

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    if out:
        out.release()
    video.release()
    cv2.destroyAllWindows()


# Upload recorded video to IPFS and log the hash
def upload_to_ipfs(file):
    try:
        client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")
        result = client.add(file)
        print("IPFS HASH:", result['Hash'])
        return result['Hash']
    except Exception as e:
        print(f"Error uploading to IPFS: {e}")
        return None


# Process videos and interact with the smart contract
def process_videos(contract):
    output_dir = './record_videos'
    metadata_file = 'ipfs.txt'

    with open(metadata_file, 'w') as f:
        for file in os.listdir(output_dir):
            if file.endswith('.mp4'):
                file_path = os.path.join(output_dir, file)
                ipfs_hash = upload_to_ipfs(file_path)
                if ipfs_hash:
                    timestamp = int(os.path.getmtime(file_path))
                    f.write(f"{ipfs_hash},{timestamp}\n")
                    send_to_blockchain(contract, ipfs_hash, timestamp)



def send_to_blockchain(contract, ipfs_hash, timestamp):
    w3, contract = connect_to_contract()
    wallet_address = w3.eth.accounts[0] 

    # Build and sign the transaction
    nonce = w3.eth.getTransactionCount(wallet_address)
    transaction = contract.functions.addrecord(ipfs_hash, timestamp).buildTransaction({
        'chainId': 1337,  
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'from': wallet_address,
        'nonce': nonce
    })

    private_key = ''  # put  your private key here
    signed_txn = w3.eth.account.signTransaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f"Transaction hash: {tx_hash.hex()}")


if __name__ == "__main__":
    w3, contract = connect_to_contract()
    record_video()
    process_videos(contract)
