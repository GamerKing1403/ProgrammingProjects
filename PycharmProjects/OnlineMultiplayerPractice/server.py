import socket
from _thread import *
from player import Player
import pickle 


server = "192.168.0.101"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(0, 0, 100, 100, (0, 255, 0)), Player(400, 400, 100, 100, (0, 0, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                elif player == 0:
                    reply = players[1]

            conn.sendall(pickle.dumps(reply))
        except socket.error as err:
            print(err)
            break
        except ValueError as err:
            break

    print("Lost connection")
    player -= 1
    conn.close()


currentPlayer = 0

while True:
    connection, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (connection, currentPlayer,))
    currentPlayer += 1
