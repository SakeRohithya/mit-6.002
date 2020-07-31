import random
from math import *
class Location(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def distance(self,other):
        ox,oy=other.x,other.y
        xDist = self.x -ox
        yDist = self.y - oy
        return pow((xDist**2 + yDist**2),0.5)
    

class Field(Location):
    def __init__(self):
        self.drunks={}
    def addDrunk(self,drunk,location):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        self.drunks[drunk] = location
    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist,yDist=drunk.takestep()
        curLoc = self.drunks[drunk]
        self.drunks[drunk]=curLoc.move(xDist,yDist)
    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
class UsualDrunk(Drunk):
    def takestep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
def walk(f,d,numsteps):
    start = f.getLoc(d)
    for s in range(numsteps):
        f.moveDrunk(d)
    return start.distance(f.getLoc(d))
lo = Location(0,0)
f=Field()
Homer = UsualDrunk()
f.addDrunk(Homer,lo)
print(walk(f,Homer,1))
    
