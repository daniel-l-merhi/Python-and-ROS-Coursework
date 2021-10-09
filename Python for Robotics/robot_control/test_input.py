from robot_control_class import RobotControl

rc = RobotControl()

reading = int(input('Enter a number between 0 and 719: '))
laser_reading = rc.get_laser(reading)
print(laser_reading)
