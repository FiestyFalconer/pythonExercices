import cv2
import robomaster
from robomaster import robot


def main():
    ep_robot = robot.Robot()

    ep_robot.initialize(conn_type="ap")

    version = ep_robot.get_version()
    print("Robot version: {0}".format(version))

    ep_camera = ep_robot.camera

    ep_camera.start_video_stream(display=False)
    while True:
        img = ep_camera.read_cv2_image()
        cv2.imshow("Robot", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()

    ep_robot.close()


main()
