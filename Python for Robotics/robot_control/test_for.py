#! /usr/bin/env/ python

from robot_control_class import RobotControl

rc = RobotControl()
laser_readings = rc.get_laser_full()
count = 0

for x in laser_readings:
    temp_highest_value = x

    if temp_highest_value < laser_readings[count]:
        highest_value = laser_readings[count]
        count += 1
    
    elif temp_highest_value > laser_readings[count]:
        highest_value = temp_highest_value

    else:
        highest_value = temp_highest_value
        count += 1

print ("Greatest distance measured: %f" % highest_value)