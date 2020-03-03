
import math
import time
from random import randint


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
	def __str__(self):
                return str(self.x)+ "," + str(self.y)


DELTA = 5

# def rrt(startX, startY, destX, destY):

MAX_X = 1000
MIN_X = -1000
MAX_Y = 1000
MIN_Y = -1000
	

def generateNode(root, destX, destY, obsts):
	node = None
	while node == None or not valid(root, node, obsts):
		node = rrtNode(destX, destY, None)
		if randint(0, 10) < 7:
			node = rrtNode(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y), None)
		steer(root, node, destX, destY, obsts)
	return node


#Determine if the child is in a valid location
def valid(nodeParent, nodeChild, obsts):
	obstacleArray = checkObstacles(nodeParent.x, nodeParent.y, nodeChild.x, nodeChild.y, obsts)
	if len(obstacleArray) == 0:
		return True
	else:
		return False

#Find the nearest node to the child node
# def nearestPoint(nodeRoot, nodeChild):

#Take the nearest node and move the child to within the distance DELTA of it
# def steer(nodeChild):
#def rrt(startX, startY, destX, destY):

#Determine if the child is in a valid location
#def valid(nodeChild, obsts):

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

def nodeswithindistance(r,x,y,root):
        a = []
        
        if(((root.x-x)**2+(root.y-y)**2)**.5 <= r):
                a += [root]
        for child in root.children :
                a += nodeswithindistance(r,x,y,child)
                 
        return a
        

#Take the nearest node and move the child to within the distance DELTA of the nearest node
def steer(nodeRoot, nodeChild, destX, destY, obsts):
	nearest = nearestPoint(nodeRoot, nodeChild)
	direction = math.atan2(nodeChild.y - nearest.y, nodeChild.x - nearest.x)
	if ((nodeChild.x - nearest.x)**2 + (nodeChild.y - nearest.y)**2)**0.5 > DELTA:

		nodeChild.x = nearest.x + (DELTA * math.cos(direction))
		nodeChild.y = nearest.y + (DELTA * math.sin(direction))
	if valid(nodeRoot, nodeChild, obsts):
		nearest.children += [nodeChild]
		nodeChild.parent = nearest

def optimization(listNode, obsts):
	optimizedArray = [listNode[0]]
	for l in range(1, len(listNode)):
		j = 0
		if len(checkObstacles(listNode[j][0], listNode[j][1], listNode[l][0], listNode[l][1], obsts)) != 0:
			optimizedArray.append(listNode[l-1])
			j = l
			l += 1
	optimizedArray.append(listNode[len(listNode)-1])
	return optimizedArray

# def newPath(listNode):
# 	newListNode = [listNode[0]]
# 	l = 2
# 	for l in listNode:
# 		nodeswithindistance(5,l[0],l[1])



def rrt(startX, startY, destX, destY, obsts):
	startTime = time.time()
	root = rrtNode(startX, startY, None)
	end = rrtNode(destX, destY, None)
	curNode = generateNode(root, destX, destY, obsts)
	while(len(checkObstacles(curNode.x, curNode.y, destX, destY, obsts)) != 0):
		curNode = generateNode(root, destX, destY, obsts)
		costComparison(root, curNode)
	end.parent = curNode
	curNode.children += [end]
	print("HERE")
	for i in range(150):
		curNode = generateNode(root, destX, destY, obsts)
		costComparison(root, curNode)
	print("Search time: " + str(time.time() - startTime) + " seconds")
	print("Nodes generated: " + str(sizeOfTree(root)))
	print("Total path length: " + str(cost(end)))
	return optimization(getPathtoPoint(end), obsts)

def sizeOfTree(root):
	amount = 1
	for child in root.children:
		amount += sizeOfTree(child)
	return amount

def cost(node):
	if node.parent == None:
		return 0
	return ((node.x - node.parent.x)**2 + (node.y - node.parent.y)**2)**.5 + cost(node.parent)


#def costComparison(nodeParent, newNode):
#	x = 0
#	y = 1
#	betterCost = []
#	for nodes in nodeswithindistance(nodeParent):
#		if cost(nodeswithindistance(nodeParent)[x]) > cost(nodeswithindistance(nodeParent)[y]):
#			betterCost.append(nodeswithindistance(nodeParent)[y])
#			y +=1
#		else:
#			betterCost.append(nodeswithindistance(nodeParent)[x])
#			x = y
#			y +=1
#
#	return betterCost[len(betterCost)-1]


def costComparison(nodeParent, newNode):
	a = nodeswithindistance(15, newNode.x, newNode.y, nodeParent)
	originalParent = []
	newParent = []
	bestNode = []
	t = 0
	for z in a:
		oldCost = cost(z)
		distToZ = ((z.x - newNode.x) ** 2 + (z.y - newNode.y) ** 2) ** .5
		newCost = cost(newNode) + distToZ
		if oldCost > newCost:
			z.parent.children.remove(z)
			z.parent = newNode
			newNode.children.append(z)




#root = rrtNode(3,3,None)
#Node2 = rrtNode(2,2,root)
#Node3 = rrtNode(1,1,Node2)
#Node4 = rrtNode(5,-1,root)
#Node5 = rrtNode(3,1,Node4)
#Node6 = rrtNode(5,1,Node4)
#root.children = [Node2,Node4]
#Node4.children = [Node5,Node6]
#Node2.children = [Node3]
#Nodetarget = rrtNode(5,0,None)

#print(nearestPoint(root,Nodetarget).x)
#print(getPathtoPoint(Node5))
#for i in nodeswithindistance(5,0,0,root):
#       print(i)


#print(cost(Node5))

testObsts = [(0, 1.25, 1), (1.25, 0, 1), (50, 50, 20), (100, 75, 25), (500, 200, 30)]
#for i in range(10, 100, 10):
#	for j in range(10, 100, 10):
#		x = j + (5 * ((i % 20)/10))
#		testObsts += [(x, i, 2.5)]

print(rrt(0, 0, 120, 120, testObsts))


a = open("linkwaypoints.txt","w")
b = rrt(0, 0, 120, 120, testObsts)
for j in range(len(b)):
        a.write(str(j) + "\t0\t0\t16\t0\t20\t0\t0\t" + str(b[j][0]) + "\t" + str(b[j][1]) + "\t400\t1\n")

