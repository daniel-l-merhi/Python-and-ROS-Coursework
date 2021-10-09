#! /usr/bin/env python

import rospy
import time
import std_msgs
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_square_custom has been called")
    j = 1
    while j <= request.repetitions:
        i = 0
        while i < 4: 
            single_side(request.side * j)
            turn()
            i += 1
        j += 1
        
    move_square.linear.x = 0
    move_square.angular.z = 0
    my_pub.publish(move_square)
    rospy.loginfo("Finished service move_bb8_square_custom")
    
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

def single_side(size):
    move_square.linear.x = 0.2 * size
    move_square.angular.z = 0
    straight_rate = 1.5 * size
    my_pub.publish(move_square)
    time.sleep(round(straight_rate))
    move_square.linear.x = 0
    my_pub.publish(move_square)

def turn():
    move_square.linear.x = 0
    move_square.angular.z = 0.33
    my_pub.publish(move_square)
    time.sleep(turn_rate)
    move_square.angular.z = 0
    my_pub.publish(move_square)

rospy.init_node('service_move_square_custom_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback) # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_square = Twist()
rospy.loginfo("Service /move_bb8_square_custom Ready")
turn_rate = 5.0
rospy.spin()