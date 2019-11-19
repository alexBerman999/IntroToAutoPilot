import math
from random import randint
from math import sqrt

def distance(x1, y1, x2, y2, x3, y3):
	a = y1 - y2
	b = x2 - x1
	c = (x1*y2) - (x2*y1)
	distEqTop = abs(a*x3 + b*y3 + c) #Distance Equation Top Fragment
	distEqBot = (a**2 + b**2)**.5 #Distance Equation Bottom Fragment
	distEq= distEqTop/distEqBot #Distance Equation
	return(distEq)
	#return(distEq)

def checkObstacles(x1, y1, x2, y2, obsts):
	obstaclesArray = []
	a = y1 - y2
	b = x2 - x1
	c = (x1*y2) - (x2*y1)
	x = min(x1, x2)
	while x < max(x1, x2):
		y = ((-1 * a * x) + (-1 * c))/b
		for obstacle in obsts:
			if obstacle[2] >= ((x - obstacle[0]) ** 2 + (y - obstacle[1]) ** 2)**	0.5:
				if obstacle not in obstaclesArray:
					obstaclesArray.append(obstacle)
		x += 0.01
	return obstaclesArray	


testarray = [(0,20,11.181), (1,2,20), (900,900,1)]
#print(checkObstacles(0,0,10,20,testarray))

class rrtNode:
	
	def __init__(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent
		self.children = []

DELTA = 5
MAX_X = 10000
MIN_X = -10000
MAX_Y = 10000
MIN_Y = -10000
	

def generateNode(root, destX, destY, obsts):
	node = None
	while node == None or not valid(root, node, obsts):
		node = rrtNode(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y), None)
		steer(root, node, destX, destY, obsts)
	node.parent.children += [node]
	
	return node

#Determine if the child is in a valid location
def valid(nodeParent, nodeChild, obsts):
	obstacleArray = checkObstacles(nodeParent.x, nodeParent.y, nodeChild.x, nodeChild.y, obsts)
	if len(obstacleArray) == 0:
		return True
	else:
		return False

#Find the nearest node to the child node
def nearestPoint(nodeRoot, nodeChild):
        d = 0;
        minnode = nodeRoot;
        
        mind = ((nodeRoot.x-nodeChild.x)**2 + (nodeRoot.y-nodeChild.y)**2)**.5;
        for child in nodeRoot.children:
                nearestchild = nearestPoint(child,nodeChild)
                d = ((nearestchild.x-nodeChild.x)**2 + (nearestchild.y-nodeChild.y)**2)**.5
                if(d < mind):
                        mind = d
                        minnode = nearestchild
        return minnode
        
def getPathtoPoint(node):
        a = []
        b = node
        while(b != None):
                a += [(b.x,b.y)]
                b = b.parent
        a = a[::-1]
        return a
        
   


#Take the nearest node and move the child to within the distance DELTA of the nearest node
def steer(nodeRoot, nodeChild, destX, destY, obsts):
	nearest = nearestPoint(nodeRoot, nodeChild)
	direction = math.atan2(nodeChild.y - nearest.y, nodeChild.x - nearest.x)
	if ((nodeChild.x - nearest.x)**2 + (nodeChild.y - nearest.y)**2)**0.5 > DELTA:
		nodeChild.x = DELTA * math.cos(direction)
		nodeChild.y = DELTA * math.sin(direction)
	if valid(nodeRoot, nodeChild, obsts):
		nearest.children += [nodeChild]
		nodeChild.parent = nearest

def rrt(startX, startY, destX, destY, obsts):
	root = rrtNode(startX, startY, None)
	end = rrtNode(destX, destY, None)
	curNode = generateNode(root, destX, destY, obsts)
	while(len(checkObstacles(curNode.x, curNode.y, destX, destY, obsts)) != 0):
		curNode = generateNode(root, destX, destY, obsts)
	end.parent = curNode
	curNode.children += [end]
	return getPathtoPoint(end)

root = rrtNode(3,3,None)
Node2 = rrtNode(2,2,root)
Node3 = rrtNode(1,1,Node2)
Node4 = rrtNode(5,-1,root)
Node5 = rrtNode(3,1,Node4)
Node6 = rrtNode(5,1,Node4)
root.children = [Node2,Node4]
Node4.children = [Node5,Node6]
Node2.children = [Node3]
Nodetarget = rrtNode(5,0,None)

testObsts = [(-1.25, 1.25, 1), (0, 1.25, 1), (1.25, 1.25, 1), (-1.25, 0, 1), (-1.25, -1.25, 1), (1.25, 0, 1), (1.25, -1.25, 1)]
#testObsts = [(3, 3, 1)]

print(rrt(0, 0, 5, 5, testObsts))
