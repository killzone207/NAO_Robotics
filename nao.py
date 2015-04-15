# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 18:42:35 2015

@author: killz_000
"""
import sys
from naoqi import ALProxy
from sympy import *

#%%

Stance = 0
LJab = 1
RJab = 2
Block = 3
LUppercut = 4
RUppercut = 5

LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
LArmAngles = [[100, 0.5, -90, -88.5, -90], [-15, 0.5, -0.5, -2, 0], [114.5, 0.5, -90, -88.5, -90], [-10, 0.5, -90, -75, -90], [-20, 0.5, -90, -45, -90], [114.5, 0.5, -98, -88.5, -90]]
RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
RArmAngles = [[100, -0.5, 90, 88.5, 90], [114.5, -0.5, 98, 88.5, 90], [-15, -0.5, 0.5, 2, 0], [-9, -0.5, 55, 75, 90], [114.5, -0.5, 98, 88.5, 90], [-20, -0.5, 90, 45, 90]]
LLeg = ["LHipYawPitch", "LHipPitch", "LHipRoll", "LKneePitch", "LAnklePitch", "LAnkleRoll"]
LLegAngles = [[0, -50, 2.5, 80, -36, -3], [0, 0, 0, 0, 0, 0]]
RLeg = ["RHipYawPitch", "RHipPitch", "RHipRoll", "RKneePitch", "RAnklePitch", "RAnkleRoll"]
RLegAngles = [[0, -50, -2.5, 80, -36, 3], [0, 0, 0, 0, 0, 0]]

fractionMaxSpeed = 0.2

print LArmAngles[Stance]

#motion.setAngles(LArm, LArmAngles[Block], fractionMaxSpeed)

#%%
def StiffnessOn(proxy):
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def forkin(bodypart, target):
    global LeftArm, RightArm, LeftLeg, RightLeg
    the1 = 0.0
    the2 = 0.0
    the3 = 0.0
    the4 = 0.0
    __T = [[]]
    
    if bodypart == LeftArm or bodypart == RightArm:
        # inverse kinematics of ARM
        UPPER = 105.0
        LOWER = 55.95
        ELBOW = 15.00
        
        __T[0][0] = c(the4)*s(the1)*s(the3) + c(the1)*(c(the2)*c(the3)*c(the4) - s(the2)*s(the4))
        __T[0][1] = c(the3)*c(the4)*s(the2) + c(the2)*s(the4)
        __T[0][2] = -c(the2)*c(the3)*c(the4)*s(the1) + c(the1)*c(the4)*s(the3) + s(the1)*s(the2)*s(the4)
        __T[0][3] = -ELBOW*c(the3)*c(the4) + UPPER*s(the4)
        __T[1][0] = -s(the1)*s(the3)*s(the4) - c(the1)*(c(the4)*s(the2) + c(the2)*c(the3)*s(the4))
        __T[1][1] = c(the2)*c(the4) - c(the3)*s(the2)*s(the4)
        __T[1][2] = c(the4)*s(the1)*s(the2) + s(the4)*(c(the2)*c(the3)*s(the1) - c(the1)*s(the3))
        __T[1][3] = UPPER*c(the4) + ELBOW*c(the3)*s(the4)
        __T[2][0] = c(the3)*s(the1) - c(the1)*c(the2)*s(the3)
        __T[2][1] = -s(the2)*s(the3)
        __T[2][2] = c(the1)*c(the3) + c(the2)*s(the1)*s(the3)
        __T[2][3] = ELBOW*s(the3)
        
        if bodypart == LeftArm:
            # left arm
            print __T[0][0]

    elif bodypart == LeftLeg or bodypart == RightLeg:
        # inverse kinematics of LEG
        THIGH = 100.00
        TIBIA = 102.90
        FOOT = 45.19


def main(robotIP):
    # init proxies
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could notcreate proxy to ALMotion"
        print "Error was: ", e
        
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    
    StiffnessOn(motionProxy)
    
    postureProxy.goToPosture("StandInit", 0.5)
    

if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python motiuon_poseInit.pyrobotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]
        
    main(robotIp)