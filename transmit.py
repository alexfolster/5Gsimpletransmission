# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import time
import cv2
import sys

# Check if a file name is provided as the second argument
if len(sys.argv) < 4:
   print("usage: python3 transmit.py <video_file> <client_ip> <test #>")
   sys.exit(1)

video_source = sys.argv[1]
client_ip = sys.argv[2]
test_num = sys.argv[3]

opt = {"CAP_PROP_FPS": 30}
stream = VideoGear(source=video_source, **opt).start()

server = NetGear(
    address=client_ip,
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
        frame_sizes.append(height*width*depth*8)
        transmit_array.append(int(round(time.time_ns()/100000)))  #time in ms
        server.send(frame)
        
    except KeyboardInterrupt:
        break

file_name = 'transmit_times_' + str(test_num) + '.txt'
for i in range(len(transmit_array)):
    with open(file_name, 'a') as f:
        print(f'{transmit_array[i]},{frame_sizes[i]}', file=f)

stream.stop()
server.close()