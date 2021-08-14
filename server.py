import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '10.0.0.227'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]
previous_move = "-1,-1,-1"
turn = 0
def threaded_client(conn):
    global currentId, pos, previous_move, turn
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        # try:
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
              if arr[1] == "update":
                previous = previous_move.split(",")
                if previous_move[0:2] == "-1":
                  conn.send(str.encode("0,0,0,0"))
                  continue
                else:
                  if int(previous[0]) == nid:
                    reply = previous_move
                    print("sending: " + reply)
                    conn.sendall(str.encode(reply))
                    continue
                  elif int(previous[0]) == id:
                    reply = previous_move
                    print("Sending: " + reply)
                    conn.sendall(str.encode(reply))
                    continue
              elif arr[1] != "update":
                if turn == 0:
                  turn = 1
                else:
                  turn = 0
                previous_move = reply + "," + str(turn)
          #     reply = str(nid) +
          #     reply = pos[nid][:]
          #     print("Sending: " + reply)
          #
          print("Sending: " + reply)
          conn.sendall(str.encode(reply))
        # except:
        #     break

    print("Connection Closed")
    print(addr)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))