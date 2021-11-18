import robomaster
from robomaster import robot

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="ap")

ep_led = ep_robot.led

print(ep_led)
ep_led.set_led(r=255, g=0, b=0)

ep_version = ep_robot.get_version()

print("Robot Version: {0}".format(ep_version))
ep_robot.close()