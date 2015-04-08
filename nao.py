# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 18:42:35 2015

@author: killz_000
"""

#import naoqi
from sympy import *

#%% constants definition

LeftArm = 0
RightArm = 1
LeftLeg = 2
RightLeg = 3

#%% just an example on how to use the math lib within a function

def testfunction():
    y = cos(pi)
    return y
    
print "y=", testfunction()

#%% shortcuts trig functions

def c(rad):
    return cos(rad)
def s(rad):
    return sin(rad)

    
#%% inverse kinematics

def invkin(bodypart, target):
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

#%%