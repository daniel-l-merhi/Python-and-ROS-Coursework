#! /usr/bin/env/ python

from robot_control_class import RobotControl

rc = RobotControl()
forward_range = rc.get_laser(360)

while forward_range > 1.0:
    rc.move_straight()
    forward_range = rc.get_laser(360)
    print ("Current distance to wall: %f" % forward_range)

rc.stop_robot()