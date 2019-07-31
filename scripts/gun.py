#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
from time import sleep


class Gun:
    def __init__(self):
        self.sub = rospy.Subscriber("/pushed", Bool, self.gunCallback)
        self.gunStatus = False

    def gunCallback(self, msg):
        self.gunStatus = msg
        print(self.gunStatus)

    def getGunStatus(self):
        #print("Current Status is " + str(self.gunStatus))
        sleep(0.5)
        return self.gunStatus

    def waitForGun(self):
        while not self.getGunStatus():
            print("Not yet")
            sleep(0.1)

if __name__ == "__main__":
    rospy.init_node("gun_subscriber", anonymous=True)
    gun = Gun()
    gun.waitForGun()

    print("It escaped")

"""
    myGunClass = Gun()
    pushed = False

    while True:
        if myGunClass.getGunStatus():
            print("It went to true")
            pushed = True
            break
        elif not myGunClass.getGunStatus():
            print("Current Status: " + str(myGunClass.getGunStatus()))

    while not pushed:
        rospy.spin()
"""


