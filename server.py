"""Code from Tim Ruscica, modified by Nicholas Leskovec"""
import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '0.0.0.0'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
players = []
def threaded_client(conn):
    global currentId, players
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        if len(players) < 2:
            continue
        data = conn.recv(2048)
        reply = data.decode('utf-8')
        if not data:
            conn.send(str.encode("Goodbye"))
            break
        else:
            print("Recieved: " + reply)
            arr = reply.split(",")
            id = int(arr[0])
            if id == 0: nid = 1
            if id == 1: nid = 0
            reply = reply[2::]  # Shaves off the player ID and comma and sends to other player
            print("Sending: " + reply + "to player" + str(nid))
            players[nid].sendall(str.encode(reply))
            continue

    print("Connection Closed")
    print(addr)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    players.append(conn)

    start_new_thread(threaded_client, (conn,))