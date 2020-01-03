import SocketServer
import socket
import sys

class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
##    HOST, PORT = "192.168.0.10", 10002
##    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
##    server.serve_forever()
    #for init remote udp listen
    remoteHOST, remotePORT = "192.168.0.5", 10005
    sentdata = "123456"
    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # As you can see, there is no connect() call; UDP has no connections.
    # Instead, data is directly sent to the recipient via sendto().
    sock.sendto(sentdata + "\n", (remoteHOST, remotePORT))
    received = sock.recv(1024)
    
    print "Sent:     {}".format(sentdata)
    print "Received: {}".format(received)
