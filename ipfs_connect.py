import ipfshttpclient
import os


def upload_to_ipfs(file):
    #client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    if not os.path.exists(file):
        print("file not found",file);
        return False

    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    
    result = client.add(file)
    print("IPFS HASH:", result['Hash'])
    return result['Hash']

file_path = './access_the_cam.py'
ipfshash = upload_to_ipfs(file_path)


