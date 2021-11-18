import time
import keyboard
from robomaster import camera
from robomaster import robot

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")
ep_chassis = ep_robot.chassis


def move():

    if keyboard.is_pressed('w'):  # if key 'q' is pressed
        ep_chassis.move(x=0.1, y=0, z=0, xy_speed=3.5, z_speed=180)

    if keyboard.is_pressed('s'):  # if key 'q' is pressed
        ep_chassis.move(x=-0.1, y=0, z=0, xy_speed=3.5, z_speed=180)

    if keyboard.is_pressed('d'):  # if key 'q' is pressed
        ep_chassis.move(x=0, y=0.1, z=0, xy_speed=3.5, z_speed=180)

    if keyboard.is_pressed('a'):  # if key 'q' is pressed
        ep_chassis.move(x=0, y=-0.1, z=0, xy_speed=3.5, z_speed=180)


while True:
    move()

ep_robot.close()
