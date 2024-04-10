# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import time

opt = {"CAP_PROP_FPS": 30}
stream = VideoGear(source="test.mp4", **opt).start()


server = NetGear(
    address="127.0.0.1",
    port="5454",
    protocol="tcp",
    pattern=0,
    logging=True
)

transmit_array = []
frame_sizes = []
while True:

    try:
        # read frames from stream
        frame = stream.read()

        # check for frame if Nonetype
        if frame is None:
            break
        
        height, width, depth = frame.shape
        frame_sizes.append(height*width*depth)
        transmit_array.append(int(round(time.time() * 1000)))  #time in ms
        server.send(frame)
        
    except KeyboardInterrupt:
        break

for i in range(len(transmit_array)):
    with open('transmit_times.txt', 'a') as f:
        print(f'{transmit_array[i]},{frame_sizes[i]}', file=f)

stream.stop()
server.close()