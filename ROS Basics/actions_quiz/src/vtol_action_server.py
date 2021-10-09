#! /usr/bin/env python

import rospy
import actionlib
import time

from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgAction, CustomActionMsgResult
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class VTOL (object):
    _feedback = CustomActionMsgFeedback()
    _result = CustomActionMsgResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer("/action_custom_msg_as", CustomActionMsgAction, self.callback, False)
        self._as.start()
        self.t = Twist()
        self.e = Empty()
        self.takeoff_msg = Empty()
        self.takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size = 1)
        self.land_msg = Empty()
        self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size = 1)
        self.r = rospy.Rate(1)

    def callback(self, goal):
        success = False
        while success == False:
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                self._as.set_preempted()
                success = False
                break
            
            if goal.goal == 'TAKEOFF':
                self.takeoff_pub.publish(self.takeoff_msg)
                success = True
            elif goal.goal == 'LAND':
                self.land_pub.publish(self.land_msg)
                success = True

            self._feedback.feedback = goal.goal
            self._as.publish_feedback(self._feedback)
            rospy.loginfo('Drone is in the %s phase', self._feedback.feedback)
            self.r.sleep()

            if success:
                self._result = self.e
                self._as.set_succeeded(self._result)
                rospy.loginfo('%s was successful!', goal.goal)

if __name__ == '__main__':
  rospy.init_node('action_custom_msg_as_node')
  VTOL()
  rospy.spin()