# 5Gsimpletransmission

Streaming of live video using python from one system to another and record latency. This is just a test to get 5G transfer working.

Required libraries:
```
pip3 install vidgear
pip3 install pyzmq
pip3 install opencv-python
```
Usage:
transmit.py
```
python3 transmit.py <file> <client_ip> <test #>
```
recieve.py
```
python3 recieve.py <client_ip> <test #>
```
Output Files are in .txt format:

<event time in ms>, <frame size in bits>
