#! /usr/bin/env python

import rospy
from move_square.srv import MoveInSquare, MoveInSquareResponse
from geometry_msgs.msg import Twist
import time

class Move:
    def __init__(self):
        self.straight_time = 3
        self.straight_speed = 0.05
        self.turn_speed = 0.32
        self.turn_time = 8

    def square(self, response):
        print("square")
        i = 0
        while i < 4:
            self.straight()
            self.turn()
            i += 1
        t.linear.x = 0
        t.angular.z = 0
        pub.publish(t)
        response_object.complete = True
        return response_object
    
    def turn(self):
        t.linear.x = 0
        t.angular.z = self.turn_speed
        pub.publish(t)
        time.sleep(self.turn_time)
    
    def straight(self):
        t.linear.x = self.straight_speed
        t.angular.z = 0
        pub.publish(t)
        time.sleep(self.straight_time)

t = Twist()
m = Move()
response_object = MoveInSquareResponse()
rospy.init_node('service_move_in_square_server_node')
square_service = rospy.Service('/move_in_square', MoveInSquare, m.square)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
rospy.spin()