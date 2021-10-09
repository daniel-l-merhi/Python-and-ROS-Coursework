#! /usr/bin/env python

import rospy
import actionlib
import time

from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from actionlib.msg import TestFeedback, TestResult, TestAction

class SquareClass(object):
    # create messages that are used to publish feedback/result
    _feedback = TestFeedback()
    _result   = TestResult()

    def __init__(self):
        # creates the action server
        self._as = actionlib.SimpleActionServer("move_drone_square", TestAction, self.goal_callback, False)
        self._as.start()
        self.t = Twist()
        self.e = Empty()
        self.r = rospy.Rate(1)
        self.takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size = 1)
        self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size = 1)
        self.drone_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
        self.t.linear.x = 0.2
        self.side = 1

    def goal_callback(self, goal):
        success = True
        self.takeoff_pub.publish(self.e)
        sideSize = goal.goal
        start_time = time.time()
        # starts moving drone
        while self.side <= 4:
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                # set the client in preempted state (goal cancelled)
                self._as.set_preempted()
                success = False
                # end the movement
                break
            
            rospy.loginfo('"move_square_drone": Executing side %i of square' % self.side)
            self.move_straight(sideSize)
            self.turn()
            self.side += 1
            # builds the next feedback msg to be sent
            self._feedback.feedback = self.side
            # publish the feedback
            self._as.publish_feedback(self._feedback)
            # the sequence is computed at 1 Hz frequency
            # self.r.sleep()
        
        # at this point, either the goal has been achieved (success==true)
        # or the client preempted the goal (success==false)
        # If success, then we publish the final result
        # If not success, we do not publish anything in the result
        if success:
            self._result.result = self._feedback.feedback
            completion_time = time.time() - start_time
            rospy.loginfo('Succeeded moving drone in square of size %i' % sideSize )
            rospy.loginfo('Time to complete was %i seconds' %completion_time)
            self._as.set_succeeded(self._result)
            self.land_pub.publish(self.e)
    
    def move_straight(self, size):
        self.t.linear.x = 0.2
        self.t.linear.x *= size
        self.drone_pub.publish(self.t)
        i = 0
        while i < 3:
            self.r.sleep()
            i += 1
        self.t.linear.x = 0
        self.drone_pub.publish(self.t)
    
    def turn (self):
        self.t.angular.z = 0.4
        self.t.linear.x = 0
        self.drone_pub.publish(self.t)
        i = 0
        while i < 3:
            self.r.sleep()
            i += 1 
        self.t.angular.z = 0
        self.t.linear.x = 0
        self.drone_pub.publish(self.t)

      
if __name__ == '__main__':
  rospy.init_node('move_square_drone_node')
  SquareClass()
  rospy.spin()