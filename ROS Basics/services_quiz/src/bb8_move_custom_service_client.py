#! /usr/bin/env python

import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_square_custom_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_square_custom_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
move_square_custom_request_object = BB8CustomServiceMessageRequest()

"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the circle
int32 repetitions    # The number of times BB-8 has to execute the circle movement when the service is called
---
bool success         # Did it achieve it?
"""
move_square_custom_request_object.repetitions = 3
move_square_custom_request_object.side = 2

rospy.loginfo("Doing Service Call...")
result = move_square_custom_client(move_square_custom_request_object)
rospy.loginfo(str(result))
rospy.loginfo("END of Service call...")
