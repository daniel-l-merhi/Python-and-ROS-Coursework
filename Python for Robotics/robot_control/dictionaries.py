#! /usr/bin/env/ python

from robot_control_class import RobotControl

rc = RobotControl()

laser_readings = rc.get_laser_full()

dict = {"Position 0: ": laser_readings[0], 
        "Position 100: ": laser_readings[100],
        "Position 200: ": laser_readings[200],
        "Position 300: ": laser_readings[300],
        "Position 400: ": laser_readings[400],
        "Position 500: ": laser_readings[500],
        "Position 600: ": laser_readings[600],
        "Position 719: ": laser_readings[719]}
print(dict)