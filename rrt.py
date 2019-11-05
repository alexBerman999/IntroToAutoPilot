class rrtNode:
	def rrtNode(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent

DELTA = 20

def rrt(startX, startY, destX, destY):

#Determine if the child is in a valid location
def valid(nodeChild):

#Find the nearest node to the child node
def nearestPoint(nodeRoot, nodeChild):

#Take the nearest node and move the child to within the distance DELTA of it
def steer(nodeChild):

