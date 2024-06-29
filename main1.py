import cv2
import datetime
import time
import ipfshttpclient
import os

def record_video():
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detection = False
    detection_stopped_time = None
    timer_start = False
    x = 2

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
                out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
                print("Started recording!!")

        elif detection:
            if timer_start:
                if time.time() - detection_stopped_time >= x:
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

def upload_to_ipfs(file):
    

    try:
        client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001")
        result = client.add(file)
        print("IPFS HASH:", result['Hash'])
        return result['Hash']
    except Exception as e:
        print(f"Error uploading to ipfs: {e}")
        return None


def process_videos():
    output_dir = './record_videos'
    metadata_file = 'ipfs.txt'

    with open(metadata_file, 'w') as f:
        for file in os.listdir(output_dir):
            if file.endswith('.mp4'):
                file_path = os.path.join(output_dir, file)
                ipfs_hash = upload_to_ipfs(file_path)
                timestamp = int(os.path.getmtime(file_path))
                f.write(f"{ipfs_hash},{timestamp}\n")

if __name__ == "__main__":
    record_video()
    process_videos()


