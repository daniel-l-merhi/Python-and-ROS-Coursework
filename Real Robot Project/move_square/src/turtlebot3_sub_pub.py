#! /usr/bin/env python
#publish vel to turtlebot and subscribe to its laser scan data

import rospy
import rospkg
import time
from move_square.srv import MoveInSquare, MoveInSquareRequest
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class MoveRobot:
    def __init__(self):
        self.t = Twist()
        self.l = LaserScan()
        self.t.linear.x = 0.1
        self.min_wall_distance = 0.3

    def callback(self, msg):
        self.length = len(msg.ranges)
        print (self.length)

    def detect_wall(self, msg):
        self.laser_ranges = msg.ranges
        if self.laser_ranges[91] < self.min_wall_distance:
            self.t.linear.x = 0
            pub.publish(self.t)
            move_in_square_service_client.close()
            print("connection to service closed")
        else:
            self.t.linear.x = 0.1
            pub.publish(self.t)

rospy.init_node('turtlebot3_sub_pub')
rospy.wait_for_service('/move_in_square')
move_in_square_service_client = rospy.ServiceProxy('/move_in_square', MoveInSquare)
move_in_square_request_object = MoveInSquareRequest()

result = move_in_square_service_client(move_in_square_request_object)
rospy.loginfo(result)
mr = MoveRobot()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
sub = rospy.Subscriber('/scan', LaserScan, mr.detect_wall)
rospy.spin()