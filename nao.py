# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 18:42:35 2015

@author: killz_000
"""

import math
#import naoqi

#%% constants definition

LeftArm = 0
RightArm = 1
LeftLeg = 2
RightLeg = 3

#%% just an example on how to use the math lib within a function

def testfunction():
    y = math.atan(1/3**0.5) * 180/math.pi
    return y
    
print "y=", testfunction()

#%% inverse kinematics

def invkin(bodypart, target):
    global LeftArm, RightArm, LeftLeg, RightLeg
    if bodypart == LeftArm or bodypart == RightArm:
        # inverse kinematics of ARM
        UPPERARM = 105.0
        LOWERARM = 55.95
        

    elif bodypart == LeftLeg or bodypart == RightLeg:
        # inverse kinematics of LEG
        

#%%