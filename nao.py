# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 18:42:35 2015

@author: killz_000
"""
import sys
#import random
from naoqi import ALProxy

#%%

motion = ALProxy("ALMotion", "nao.local", 9559)
motion.moveInit()

Stance = 0
LJab = 1
RJab = 2
Block = 3
LUppercut = 4
RUppercut = 5

Combo = [[Stance, LJab, Stance, RJab], [Stance, LJab, RJab], [Stance, RJab, LUppercut], [Stance, LUppercut, RUppercut], [Stance, LJab, RJab, Block], [Stance, LJab, RJab, Block, RJab, LJab, Block]]

LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]
LArmAngles = [[100, 0.5, -90, -88.5, -90], [-15, 0.5, -0.5, -2, 0], [114.5, 0.5, -90, -88.5, -90], [-10, 0.5, -55, -75, -90], [-20, 0.5, -90, -45, -90], [114.5, 0.5, -98, -88.5, -90]]
RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
RArmAngles = [[100, -0.5, 90, 88.5, 90], [114.5, -0.5, 98, 88.5, 90], [-15, -0.5, 0.5, 2, 0], [-10, -0.5, 55, 75, 90], [114.5, -0.5, 98, 88.5, 90], [-20, -0.5, 90, 45, 90]]
LLeg = ["LHipYawPitch", "LHipPitch", "LHipRoll", "LKneePitch", "LAnklePitch", "LAnkleRoll"]
LLegAngles = [[0, -50, 2.5, 80, -36, -3], [0, 0, 0, 0, 0, 0]]
RLeg = ["RHipYawPitch", "RHipPitch", "RHipRoll", "RKneePitch", "RAnklePitch", "RAnkleRoll"]
RLegAngles = [[0, -50, -2.5, 80, -36, 3], [0, 0, 0, 0, 0, 0]]

fractionMaxSpeed = 0.2

#%%
def StiffnessOn(proxy):
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


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
    
    id = postureProxy.goToPosture("StandInit", 0.5)
    postureProxy.wait(id, 0)
    
    motion.setAngles(LArm, LArmAngles[0], fractionMaxSpeed)
    motion.setAngles(RArm, RArmAngles[0], fractionMaxSpeed)
    motion.setAngles(LLeg, LLegAngles[0], fractionMaxSpeed)
    id = motion.setAngles(RLeg, RLegAngles[0], fractionMaxSpeed)
    motion.wait(id, 0)
    
    for i in range(len(Combo[0])):
        for move in Combo:
            motion.setAngles(LArm, LArmAngles[move[i]], fractionMaxSpeed)
            id = motion.setAngles(RArm, RArmAngles[move[i]], fractionMaxSpeed)
            motion.wait(id, 0)
    
    #motion.setAngles(LArm, LArmAngles[Block], fractionMaxSpeed)
    

if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python motiuon_poseInit.pyrobotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]
        
    main(robotIp)