class rrtNode:
	def __init__(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent
		self.children = []

DELTA = 20

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



