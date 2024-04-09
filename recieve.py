# import required libraries
from vidgear.gears import NetGear
import cv2
import time



client = NetGear(
    address="127.0.0.1",
    port="5454",
    protocol="udp",
    pattern=0,
    receive_mode=True,
    logging=True
)

# loop over
while True:
    
    frame = client.recv()
    time_recieved = int(round(time.time() * 1000))

    # again check for frame if None
    if frame is None:
        break

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    with open('recieve_times.txt', 'a') as f:
        print(f'{time_recieved}\n', file=f)

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()