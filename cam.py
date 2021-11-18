import cv2
from robomaster import robot
import socket
import keyboard
import time

host = "192.168.2.1"
port = 40923
address = (host, int(port))

# Establish a TCP connection with the control command port of the robot.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connecting():
    print("Connecting...")

    s.connect(address)

    print("Connected!")
    msg = "command;"
    s.send(msg.encode('utf-8'))
    buf = s.recv(1024)
    print(buf.decode('utf-8'))


def move():
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


def cam():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_camera = ep_robot.camera
    ep_camera.start_video_stream(display=False)
    for i in range(0, 999999):
        img = ep_camera.read_cv2_image()
        cv2.imshow("Robot", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()


connecting()
#cam()

while True :

    move()
    time.sleep(0.3)