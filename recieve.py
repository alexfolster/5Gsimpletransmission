# import required libraries
from vidgear.gears import NetGear
import cv2
import time


options = {"bidirectional_mode": True}


client = NetGear(
    address="127.0.0.1",
    port="5454",
    protocol="udp",
    pattern=0,
    receive_mode=True,
    logging=True,
    **options
)

# loop over
while True:
    time_recieved = int(round(time.time() * 1000))
    data = client.recv(return_data=time_recieved)

    # check for data if None
    if data is None:
        break

    server_data, frame = data

    # again check for frame if None
    if frame is None:
        break

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()