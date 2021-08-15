"""Code by Tim Ruscica, modified by Nicholas Leskovec"""
import socket
import select

class Network:

    def __init__(self, ipAddr, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ipAddr # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                    # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                    # ipv4 address. This feild will be the same for all your clients.
        self.port = port
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode(data))
            print(str.encode(data))
        except socket.error as e:
            return str(e)

    def networkDataArrived(self):
        socks = [self.client]
        input, output, excep = select.select(socks, [], [], 0.01)
        if input.count(self.client) > 0:
            return True
        return False

    def receive(self):
        reply = self.client.recv(2048).decode()
        return reply

