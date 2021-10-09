#! /usr/bin/env python

import rospy
from read_odometry.msg import Age

rospy.init_node('age_pub') #initiatie the node
pub = rospy.Publisher('/age_info', Age, queue_size=1) #Create a Publisher that will publish in the /age_info topic
rate = rospy.Rate(2) #set rate at 2 Hz
age = Age() #create an age message object
age.years = 5 #fill values of message
age.months = 2
age.days = 1

while not rospy.is_shutdown():
    pub.publish(age) #publish message into topic age_info
    rate.sleep()