from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")

def return_laser(a, b, c):
    laser_list = [rc.get_laser_summit(a), rc.get_laser_summit(b), rc.get_laser_summit(c)]

    return laser_list

l = return_laser(0, 360, 400)

print (l)