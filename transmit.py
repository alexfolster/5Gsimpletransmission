# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import time

opt = {"CAP_PROP_FPS": 30}
stream = VideoGear(source="test.mp4", **opt).start()
options = {"bidirectional_mode": True}

server = NetGear(
    address="127.0.0.1",
    port="5454",
    protocol="udp",
    pattern=0,
    logging=True,
    **options
)


while True:

    try:
        # read frames from stream
        frame = stream.read()

        # check for frame if Nonetype
        if frame is None:
            break
        time_sent = int(round(time.time() * 1000)) #time in ms
        time_recieved = server.send(frame, "") # in ms

        if time_recieved != None:
            print(f"Latency: {time_recieved-time_sent}")

    except KeyboardInterrupt:
        break


stream.stop()
server.close()