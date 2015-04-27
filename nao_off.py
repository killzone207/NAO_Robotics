# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 18:42:35 2015

@author: killz_000
"""
import sys
import math
import random
import time
#import random
from naoqi import ALProxy


#%%
def StiffnessOn(proxy):
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
    
def StiffnessOff(proxy):
    pNames = "Body"
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP):
    # init proxies
    try:
        motion = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could notcreate proxy to ALMotion"
        print "Error was: ", e
    
    StiffnessOff(motion)
    

    
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