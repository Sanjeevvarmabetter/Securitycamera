from ipfshttpclient import connect

# Connect to the local IPFS daemon
ipfs = connect("/ip4/127.0.0.1/tcp/5001")

# Upload a file to IPFS
res = ipfs.add("path")
ipfs_hash = res["Hash"]
print(f"IPFS Hash: {ipfs_hash}")

#research on how to use