#! /usr/bin/env/ python

from robot_control_class import RobotControl

rc = RobotControl()
laser_readings = rc.get_laser_full()
print(laser_readings[0])
print(laser_readings[360])
print(laser_readings[719])