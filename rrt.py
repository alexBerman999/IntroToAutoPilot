from math import sqrt

def distance(x1, y1, x2, y2, x3, y3):
	a = y1 - y2
	b = x2 - x1
	c = (x1*y2) - (x2*y1)
	distEqTop = abs(a*x3 + b*y3 + c) #Distance Equation Top Fragment
	distEqBot = sqrt(a**2 + b**2) #Distance Equation Bottom Fragment
	distEq= distEqTop/distEqBot #Distance Equation
	return(distEq)
	#return(distEq)

def checkObstacles(x1, y1, x2, y2, obsts):
	obstaclesArray = []
	for obstacle in obsts:
		distance(x1, y1, x2, y2, obstacle[0], obstacle[1])
		if obstacle[2] >= distance(x1, y1, x2, y2, obstacle[0], obstacle[1]):
			obstaclesArray.append(obstacle)
	return obstaclesArray	


testarray = [(0,20,11.181), (1,2,20), (900,900,1)]
print(checkObstacles(0,0,10,20,testarray))



class rrtNode:
	
	def __init__(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent
		self.children = []

DELTA = 20

# def rrt(startX, startY, destX, destY):

#Determine if the child is in a valid location
def valid(nodeParent, nodeChild, obsts):
	checkObstacles(nodeParent.x, nodeParent.y, nodeChild.x, nodeChild.y, obsts)
	if len(obstaclesArray) == 0:
		return True
	else:
		return False
	# if nodeChild.x == obsts.x and nodeChild.y == obsts.y:
	# 	print("Warning Zone")

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
                print("Parent: (" + str(nodeRoot.x) + ", " + str(nodeRoot.y) + ")")
                print("Nearest Child: (" + str(nearestchild.x) + ", " + str(nearestchild.y) + ")")
                d = ((nearestchild.x-nodeChild.x)**2 + (nearestchild.y-nodeChild.y)**2)**.5
                print("Previous Min: " + str(mind) + "\tCurrent: " + str(d)) 
                if(d < mind):
                        mind = d
                        minnode = nearestchild
        return minnode
        
        

#Take the nearest node and move the child to within the distance DELTA of it
#def steer(nodeChild):
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
print(nearestPoint(root,Nodetarget).x)



