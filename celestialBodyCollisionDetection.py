'''
Predicting Celestial Body Collisions in Python
Nathan Tardy
3.2.2022
Bangor High School
'''

# Importing libraries
from time import sleep
from math import *
from numpy import arccos, arcsin, arctan
# import tensorflow as tf

# Variables
G = (6.67)*(10**-11) # Newtonian Gravitation Constant
distance = [0,0,0]
outcomes = []

# Functions
def vecMag(list):
    magnitude = sqrt((list[0]**2)+(list[1]**2)+(list[2]**2))
    return magnitude

class createBody():
    def __init__ (self,mass,radius,posX,posY,posZ,velX,velY,velZ):
        self.mass = mass
        self.radius = radius
        self.pos = [posX,posY,posZ]
        self.vel = [velX,velY,velZ]
        self.momentum = [(mass *velX),(mass * velY),(mass * velZ)]
    
def gravity(posA,posB):
    for index in range(3):
        distance[index] = abs(posA[index] - posB[index])
        magDistance = vecMag(distance)
        gravityForce = (G*body1.mass*body2.mass)/(magDistance**2)
        XGravity = gravityForce*sin(arcsin(abs(posA[0]-posB[0])/magDistance))
        YGravity = gravityForce*cos(arccos(abs(posA[1]-posB[1])/magDistance))
        ZGravity = gravityForce*tan(arctan(abs(posA[2]-posB[2])/magDistance))
        gravity = [XGravity,YGravity,ZGravity]
        return gravity

#for elem in range(int(5.98*(10**24))):
elem = (5.98*(10**30))
body1 = createBody(elem,20,0,0,0,0,0,0)
#for element in range(int(5.98*(10**24)),1):
element = (5*10**3)
body2 = createBody(element,20,100,0,0,0,0,0)
delta_t = 0.000001
for number in range(100000):
    if all(body2.radius >= abs(body1.pos[index] - body2.pos[index]) for index in range(3)):
        outcomes.append("Collision")
        break
    else:
        body1.gravity = gravity(body1.pos,body2.pos)
        body2.gravity = body1.gravity
        for index in range(3):
            body1.momentum[index] = body1.momentum[index] + (body1.gravity[index] * delta_t)
        for index in range(3):
            body2.momentum[index] = body2.momentum[index] + (body2.gravity[index] * delta_t)
        for index in range(3):
            body1.pos[index] = body1.pos[index] + (body1.momentum[index]/body1.mass) * delta_t
        for index in range(3):
            body2.pos[index] = body2.pos[index] + (body2.momentum[index]/body2.mass) * delta_t
    print(f"Body1: {body1.pos}, Body2: {body2.pos}")
    sleep(10)
outcomes.append("No Collision")
print(outcomes)
# Lots of stuff that needs fixing here