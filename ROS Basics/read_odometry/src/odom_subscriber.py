#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print(msg) #this will print whole odom message
    # print(msg.header) #This will print the header section of the Odometry message
    # print(msg.pose) # #This will print the pose section of the Odometry message
rospy.init_node('odom_sub_node')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
rospy.sleep

