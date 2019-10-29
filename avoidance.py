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

# checkObstacles(25,18,56,99)

# for obsts in obstacles:
# 	dist = 