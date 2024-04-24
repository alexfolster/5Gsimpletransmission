# import required libraries
from vidgear.gears import NetGear
import cv2
import time
import sys

# Check if a file name is provided as the second argument
if len(sys.argv) < 3:
   print("usage: python3 recieve.py <client_ip> <test #>")
   sys.exit(1)

client_ip = sys.argv[1]
test_num = sys.argv[2]

client = NetGear(
    address=client_ip,
    port="5454",
    protocol="udp",
    pattern=0,
    receive_mode=True,
    logging=True
)

recieve_times = []
frame_sizes = []
# loop over
while True:
    try:
        frame = client.recv()
        recieve_times.append(int(round(time.time_ns()/100000)))

        # again check for frame if None
        if frame is None:
            break

        h, w, d = frame.shape
        frame_sizes.append(h*w*d*8)

    except KeyboardInterrupt:
        break

file_name = 'recieve_times_' + str(test_num) + '.txt'
for i in range(len(frame_sizes)):
    with open(file_name, 'a') as f:
        print(f'{recieve_times[i]}, {frame_sizes[i]}', file=f)

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()