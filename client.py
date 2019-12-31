import zmq
import sys

context = zmq.Context()

sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

sock.send(b"Testing")
print(sock.recv())
