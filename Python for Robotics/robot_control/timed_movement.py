import time

from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")
move = rc.move_straight()

def move_straight(secs):
    rc.move_straight()
    time.sleep(secs)
    rc.stop_robot()

move_straight(5)