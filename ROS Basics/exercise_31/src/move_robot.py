#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_robot_node') #tells rospy name of our node
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) #Assign the handle 'pub' and publish to the cmd_vel topic using msg type Twist
rate = rospy.Rate(2) #looping at desired rate of 2 Hz
move = Twist()
move.linear.x = 0.5 #move the robot with a linear veloicty in the x axis
move.angular.z = 0.5 #move the robot with an angular velocity in the z axis

while not rospy.is_shutdown:
    pub.publish(move)
    rate.sleep