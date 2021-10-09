#! /usr/bin/env python

import rospy
import actionlib
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from record_odom.msg import OdomRecordAction

class MoveRobot:
    def __init__(self):
        t.linear.x = 0.1
        self.min_wall_distance = 0.2
        # self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        # self.sub = rospy.Subscriber('/scan', LaserScan, mr.detect_wall)
        # self.client = actionlib.SimpleActionClient('/record_odom', OdomRecordAction)
        
    def detect_wall(self, msg):
        self.laser_ranges = msg.ranges
        if self.laser_ranges[91] < 0.2:
            t.linear.x = 0
            pub.publish(self.t)
        else:
            t.linear.x = 0.1
            pub.publish(t)

# if __name__ == "__main__":
rospy.init_node('movement_node')
client = actionlib.SimpleActionClient('/record_odom', OdomRecordAction)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
mr = MoveRobot()
t = Twist()
l = LaserScan()
sub = rospy.Subscriber('/scan', LaserScan, mr.detect_wall)
print("client")
rospy.spin()