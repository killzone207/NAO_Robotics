# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 18:42:35 2015

@author: killz_000
"""
import sys
import math
#import random
from naoqi import ALProxy

#%%

Stance = 0
LJab = 1
RJab = 2
Block = 3
LUppercut = 4
RUppercut = 5

MaxArmStates = 6
MaxLegStates = 2
MaxJoints = 6

Combo = [[Stance, LJab, Stance, RJab], [Stance, LJab, RJab], [Stance, RJab, LUppercut], [Stance, LUppercut, RUppercut], [Stance, LJab, RJab, Block], [Stance, LJab, RJab, Block, RJab, LJab, Block]]

LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
LArmAngles = [[100.0, 0.5, -90.0, -88.5, -90.0, 0.0], [-15.0, 0.5, -0.5, -2.0, 0.0, 0.0], [114.5, 0.5, -90.0, -88.5, -90.0, 0.0], [-10.0, 0.5, -55.0, -75.0, -90.0, 0.0], [-20.0, 0.5, -90.0, -45.0, -90.0, 0.0], [114.5, 0.5, -98.0, -88.5, -90.0, 0.0]]
RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
RArmAngles = [[100.0, -0.5, 90.0, 88.5, 90.0, 0.0], [114.5, -0.5, 98.0, 88.5, 90.0, 0.0], [-15.0, -0.5, 0.5, 2.0, 0.0, 0.0], [-10.0, -0.5, 55.0, 75.0, 90.0, 0.0], [114.5, -0.5, 98.0, 88.5, 90.0, 0.0], [-20.0, -0.5, 90.0, 45.0, 90.0, 0.0]]
LLeg = ["LHipYawPitch", "LHipPitch", "LHipRoll", "LKneePitch", "LAnklePitch", "LAnkleRoll"]
LLegAngles = [[0.0, -50.0, 2.5, 80.0, -36.0, -3.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
RLeg = ["RHipYawPitch", "RHipPitch", "RHipRoll", "RKneePitch", "RAnklePitch", "RAnkleRoll"]
RLegAngles = [[0.0, -50.0, -2.5, 80.0, -36.0, 3.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

fractionMaxSpeed = 0.5

#%% convert 2d arrays from deg to rad
def Deg_Rad(x, states, joints):
    for i in range(states):
        for j in range(joints):
            x[i][j] = math.radians(x[i][j])

Deg_Rad(LArmAngles, MaxArmStates, MaxJoints)
Deg_Rad(RArmAngles, MaxArmStates, MaxJoints)
Deg_Rad(LLegAngles, MaxLegStates, MaxJoints)
Deg_Rad(RLegAngles, MaxLegStates, MaxJoints)



#%%
def StiffnessOn(proxy):
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP):
    # init proxies
    try:
        motion = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could notcreate proxy to ALMotion"
        print "Error was: ", e
        
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    
    StiffnessOn(motion)
    
    id = postureProxy.goToPosture("StandInit", 0.5)
    postureProxy.wait(id, 0)
    motion.moveInit()
    
    motion.setAngles(LArm, LArmAngles[0], fractionMaxSpeed)
    motion.setAngles(RArm, RArmAngles[0], fractionMaxSpeed)
    motion.setAngles(LLeg, LLegAngles[0], fractionMaxSpeed)
    id = motion.setAngles(RLeg, RLegAngles[0], fractionMaxSpeed)
    motion.wait(id, 0)
    
    i = 0
    while i < MaxArmStates:
        motion.setAngles(LArm, LArmAngles[i], fractionMaxSpeed)
        motion.setAngles(RArm, RArmAngles[i], fractionMaxSpeed)
        motion.setAngles(LLeg, LLegAngles[0], fractionMaxSpeed)
        id = motion.setAngles(RLeg, RLegAngles[0], fractionMaxSpeed)
        i += 1        
        motion.wait(id, 0)
        
    
#    for i in range(len(Combo[0])):
#        for move in Combo:
#            motion.setAngles(LArm, LArmAngles[move[i]], fractionMaxSpeed)
#            id = motion.setAngles(RArm, RArmAngles[move[i]], fractionMaxSpeed)
#            motion.wait(id, 0)
    
#    motion.setAngles(LArm, LArmAngles[Block], fractionMaxSpeed)
    

if __name__ == "__main__":
    robotIp = "169.254.226.148"

    if len(sys.argv) <= 1:
        print "Connecting to IP: 169.254.226.148"
    else:
        robotIp = sys.argv[1]
        
    main(robotIp)
    
#%%