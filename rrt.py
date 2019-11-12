import math
from random import randint

class rrtNode:
	def rrtNode(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent
		self.children = []

DELTA = 20
MAX_X = 10000
MIN_X = -10000
MAX_Y = 10000
MIN_Y = -10000

def rrt(startX, startY, destX, destY):
	root = rrtNode(startX, startY, None)
	

def generateNode(root):
	node = None
	while node == None or not valid(node):
		node = rrtNode(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y), None)
		steer(root, node)
	node.parent.children += [node]
	return node

#Determine if the child is in a valid location
def valid(nodeChild, obsts):

#Find the nearest node to the child node
def nearestPoint(nodeRoot, nodeChild):

#Take the nearest node and move the child to within the distance DELTA of the nearest node
def steer(nodeRoot, nodeChild):
	nearest = nearestPoint(nodeRoot, nodeChild)
	direction = math.atan2(nodeChild.y - nearest.y, nodeChild.x - nearest.x)
	nodeChild.x = DELTA * math.cos(direction)
	nodeChild.y = DELTA * math.sin(direction)
	#CHECK FOR VALIDITY
	#THEN INSERT
