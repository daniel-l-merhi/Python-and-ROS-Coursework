#! /usr/bin/env/ python

from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(360)
print(laser1)

laser2 = rc.get_laser(180)
print(laser2)

laser2 = rc.get_laser(0)
print(laser2)