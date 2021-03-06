
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
	print("Generating Nodes...")
	while(len(checkObstacles(curNode.x, curNode.y, destX, destY, obsts)) != 0):
		curNode = generateNode(root, destX, destY, obsts)
		costComparison(root, curNode)
	end.parent = curNode
	curNode.children += [end]
	print("Path Found. Optimizing Path...")
	for i in range(150):
		print("Adding " + str(i) + "/150 waypoints...", end="\r")
		curNode = generateNode(root, destX, destY, obsts)
		costComparison(root, curNode)
	print("Search time: " + str(time.time() - startTime) + " seconds")
	print("Nodes generated: " + str(sizeOfTree(root)))
	print("Total path length: " + str(cost(end)))
	return getPathtoPoint(end)

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



testObsts = [(0, 60, 50)]
wps = [(0, 0), (0 , 200)]

outfile = open("linkwaypoints.txt","w")
solution_path = []
for i in range(len(wps) - 1):
	points = rrt(wps[i][0], wps[i][1], wps[i+1][0], wps[i+1][1], testObsts)[0:-1]
	print(points)
	solution_path += points
solution_path += [wps[-1]]
print(solution_path)
outfile.write("QGC WPL 110\n")
for i in range(len(solution_path)):
        outfile.write(str(i) + "\t0\t0\t16\t0\t20\t0\t0\t" + str(solution_path[i][0]) + "\t" + str(solution_path[i][1]) + "\t400\t1\n")

