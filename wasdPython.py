# -*- encoding: utf-8 -*-
# Test environment: Python 3.6

import socket
import keyboard
import time

host = "192.168.2.1"
port = 40923
address = (host, int(port))

# Establish a TCP connection with the control command port of the robot.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def move():
    global s

    if keyboard.is_pressed('w'):  # if key 'w' is pressed
        commande("chassis move x 0.5")

    if keyboard.is_pressed('s'):  # if key 's' is pressed
        commande("chassis move x -0.5")

    if keyboard.is_pressed('d'):  # if key 'd' is pressed
        commande("chassis move y 0.5")

    if keyboard.is_pressed('a'):  # if key 'a' is pressed
        commande("chassis move y -0.5")


def commande(message):
    msg = message
    msg += ';'
    print(msg)
    s.send(msg.encode('utf-8'))


def main():
    print("Connecting...")

    s.connect(address)

    print("Connected!")
    msg = "command;"
    s.send(msg.encode('utf-8'))
    buf = s.recv(1024)
    print(buf.decode('utf-8'))

    while True:
        move()

        time.sleep(0.3)


if __name__ == '__main__':
    main()
