import pickle
import socket


class Network:

    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.15.10"    # Local IP address of the server
        self.port = 5555                 # Port on which the server is running
        self.addr = (self.server, self.port)
        try:
            self.p = self.connect()          # Player number
        except socket.error as e:
            print(e)

    def get_p(self):

        return self.p

    def connect(self):

        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):

        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)