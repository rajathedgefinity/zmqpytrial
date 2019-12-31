import zmq

context = zmq.Context()

sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

while True:
	message = sock.recv()
	print("Received Request: %s" % str(message))
	sock.send(b"Recieved")
	print("Echo: " + str(message))
