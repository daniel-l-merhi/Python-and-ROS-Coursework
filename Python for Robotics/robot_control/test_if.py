#! /usr/bin/env/ python

from robot_control_class import RobotControl

rc = RobotControl()
forward_range = rc.get_laser(360)

if forward_range >= 1.0:
    rc.move_straight()

elif forward_range < 1.0:
    rc.stop_robot()

print("Range to wall: ", forward_range)