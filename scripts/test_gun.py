#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def gunCallback(data):
    print("Current gun status is " + str(data.data))
    gunStatus = data.data
    if gunStatus:
        return True
    else:
        return False

def listener():
    gunstatus = False
    while True:
        rospy.init_node('gunListener', anonymous=True)
        rospy.Subscriber("pushed", Bool, gunCallback)

        print("Gun status is" + str(gunstatus))
        if gunstatus:
            break
        rospy.spin()

if __name__ == '__main__':
    listener()