"""
Python Project 1
"""
import random 
import numpy as np
import math

# 1. Create 10 points with x,y,z coordinates.

x = [-20 + 10*random.random() for i in range(10)]
y = [9./5*C + 32 for C in x]
z = [F/5 + 32 for F in y]
tablo1 = [[X,Y,Z] for X,Y,Z in zip(x, y,z)]
PointList = np.array(tablo1)
print(PointList,'\n')


# 2. Write a function that returns the distances of these points from each other.

def distanceCalculation(pointList1,pointList2):
    return ((pointList2[2]-pointList1[2])**2 + (pointList2[1]-pointList1[1])**2 +(pointList2[0]-pointList1[0])**2)**1/2

pointList1 = PointList[0]
pointList2 = PointList[1]
print((distanceCalculation(pointList1, pointList2)),'\n')

# 3. Write the function that calculates the angle in degrees when we give 3 of these points

pointList3 = PointList[2]

def angleCalculation(pointList1,pointList2,pointList3):
    vector1 = [pointList2[0]-pointList1[0],pointList2[1]-pointList1[1],pointList2[2]-pointList1[2]]
    vector2 = [pointList3[0]-pointList1[0],pointList3[1]-pointList1[1],pointList3[2]-pointList1[2]]
    m_vector1 = ((vector1[0])**2 + (vector1[1])**2 + (vector1[2])**2 ) **1/2
    m_vector2 = ((vector2[0])**2 + (vector2[1])**2 + (vector2[2])**2 ) **1/2
    degree = math.degrees(((vector1[0]*vector2[0]) + ( vector1[1]*vector2[1]) + ( vector1[2]*vector2[2])) / (m_vector1*m_vector2))
    return print(degree, '\n')

angleCalculation(pointList1, pointList2, pointList3)

# 4. Write a function that gives indices of atoms within a given radius of a point.

def neigbour (pointList1,distance):
    
    for i in range(len(PointList)):
        PointList_i = PointList[i]
        a = ( pointList1[2]- PointList_i[2])**2 + ( pointList1[1]- PointList_i[1])**2  + ( pointList1[0]- PointList_i[0])**2
        if (a < distance**2 ):
            print(PointList_i)

neigbour(pointList1, 6)