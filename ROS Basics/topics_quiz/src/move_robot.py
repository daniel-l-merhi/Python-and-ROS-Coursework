#! /usr/bin/env python

import rospy
import std_msgs
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

laser_ranges = LaserScan.ranges
move = Twist() #initialise object to access Twist variables
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) #Create publisher for Twist to cmd_vel

def move_robot (laser_ranges):
    forward_range = laser_ranges.ranges[360] #extract forward facing reading of laser
    left_range = laser_ranges.ranges[719] #extract left facing reading of laser
    right_range = laser_ranges.ranges[0] #extract right facing reading of laser

    #if all range is >= to 1 m robot will drive straight
    if forward_range >= 1.0 and right_range >= 1.0 and left_range >= 1.0:
        move.linear.x = 0.2
        move.angular.z = 0.0
        print("1")

    #if forward range is < 1 m robot will turn left
    elif forward_range < 1.0:
        move.linear.x = 0.2
        move.angular.z = 0.5 #+ve is left and -ve is right
        print("2")

    #if right range is < 1 m robot will turn left
    elif right_range < 1.0:
        move.linear.x = 0.2
        move.angular.z = 0.5
        print("3")

    #if left range is < 1 m robot will turn right
    elif left_range < 1.0:
        move.linear.x = 0.2
        move.angular.z = -0.5
        print("4")
    print("5")
    pub.publish(move)

def listener():
    rospy.init_node('topics_quiz_node') #initiate the node
    rospy.Subscriber('/kobuki/laser/scan', LaserScan, move_robot) #create subscriber to LaserScan from kobuki
    rospy.spin

while not rospy.is_shutdown():
    listener()
    rate = rospy.Rate(2)
    rate.sleep()

# #! /usr/bin/env python

# import rospy
# from sensor_msgs.msg import LaserScan

# laser_ranges = LaserScan.ranges

# def callback(laser_ranges):
#     print (laser_ranges.ranges[180])
#     rospy.sleep(0.5)

# rospy.init_node('scan_values')
# rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
# rospy.spin()
