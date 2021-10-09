#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1
t = Twist()
e = Empty()

# initializes the action client node
rospy.init_node('drone_action_client')


takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)

while takeoff_pub.get_num_connections() < 1:
    rate.sleep()

takeoff_pub.publish(e)

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1


# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)
state_result = client.get_state()

while state_result < DONE:
    rospy.loginfo("Doing Stuff while waiting for the Server to give a result....")
    rate.sleep()
    t.linear.x = 0.4
    t.linear.y = 0.4
    t.angular.z = 0.2
    pub.publish(t)
    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))

t.linear.x = 0
t.linear.y = 0
t.angular.z = 0
pub.publish(t)

# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()  # would cancel the goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
# status = client.get_state()
# check the client API link below for more info

# client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))