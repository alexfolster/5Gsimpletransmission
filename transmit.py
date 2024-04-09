# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import time

opt = {"CAP_PROP_FPS": 30}
stream = VideoGear(source="test.mp4", **opt).start()


server = NetGear(
    address="127.0.0.1",
    port="5454",
    protocol="udp",
    pattern=0,
    logging=True
)


while True:

    try:
        # read frames from stream
        frame = stream.read()

        # check for frame if Nonetype
        if frame is None:
            break
        time_sent = int(round(time.time() * 1000)) #time in ms
        server.send(frame)

        with open('transmit_times.txt', 'a') as f:
            print(f'{time_sent}\n', file=f)
    
    except KeyboardInterrupt:
        break


stream.stop()
server.close()