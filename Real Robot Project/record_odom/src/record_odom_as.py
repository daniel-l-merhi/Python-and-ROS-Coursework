#! /usr/bin/env python

import rospy
import time
import actionlib

from record_odom.msg import OdomRecordAction, OdomRecordFeedback, OdomRecordResult
# from record_odom_as_client import MoveRobot
from nav_msgs.msg import Odometry

class RecordOdom(object):
    _feedback = OdomRecordFeedback()
    _result = OdomRecordResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer('/record_odom', OdomRecordAction, self.record_callback, False)
        self._as.start()
        self.o = Odometry()
        # self.mr = MoveRobot()
        self.r = rospy.Rate(1)
        self.x = [0, 0]
        self.y = [0, 0]
        self.distances = []
        self.distance_counter = 0
        
    def record_callback(self):
        
        success = True

        if self._as.is_preempt_requested():
            rospy.loginfo('Goal cancelled')
            self._as.set_preempted()
            success = False

        self.odom_sub = rospy.Subscriber('/odom', Odometry, None, queue_size = 1)
        self._result.list[0] = self.o.pose.pose.position.x
        self._result.list[1] = self.o.pose.pose.position.y
        self._result.list[2] = self.o.pose.pose.orientation.z

        if self.distance_counter < 1:
            self.x[0] = self._result.list[0]
            self.y[0] = self._result.list[1]
            self.distance_counter += 1
        elif self.distance_counter == 2:
            self.x[1] = self._result.list[0]
            self.y[1] = self._result.list[1]
            self.distance_counter += 1
        else:
            self.distance_counter = 0
        
        x1 = self.x[0]
        x2 = self.x[1]
        y1 = self.y[0]
        y2 = self.y[1]
        result = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
        self.distances.append(result)

        self._feedback.total = sum(self.distances)
        rospy.loginfo('Total distance moved is %f', result)
        self._as.publish_feedback(self._feedback)

        if success:
            rospy.loginfo('Collecting Odometry...')
            self._as.set_succeeded(self._result)
        
        self.r.sleep()

# if __name__ == "__main__":
rospy.init_node('record_odom_node')
RecordOdom()
# mr = MoveRobot()
print("server")
rospy.spin()