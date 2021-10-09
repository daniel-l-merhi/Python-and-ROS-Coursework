
import rospy
from robot_control_class import RobotControl

rc = RobotControl()
rc.rotate(-4)

class Navigate_Maze():
    def __init__(self):
        self.rc = RobotControl()
        self.speed = 1.0
        self.clockwise = "clockwise"
        self.motion = "forward"
        self.turn_speed = 1.0

    def get_laser_pos(self):
        laser_full = self.rc.get_laser_full()
        print("Got full laser")
        return laser_full

    def navigate(self):
        print ("in navigate")
        laser_full = self.get_laser_pos()
        if self.rc.get_front_laser() < 1.0:
            print("wall too close")
            self.rc.stop_robot()
            if laser_full[0] > 2.0 and laser_full[719] < 2.0:
                print("turning right")
                self.rc.rotate(85)
                self.rc.stop_robot()
            if laser_full[0] < 2.0 and laser_full[719] > 2.0:
                print("turning left")
                self.rc.rotate(-85)
                self.rc.stop_robot()
        elif self.rc.get_front_laser() > 1.0:
            self.rc.move_straight()
nm = Navigate_Maze()

while not rospy.is_shutdown():
    nm.navigate()
