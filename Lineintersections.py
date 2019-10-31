import math

def sortByX(points, reverse):
	for i in range(len(points) - 1):
		for j in range(1, len(points)):
			if reverse:
				if points[i][0] < points[j][0]:
					temp = points[i]
					points[i] = points[j]
					points[j] = temp
			else:
				if points[i][0] > points[j][0]:
					temp = points[i]
					points[i] = points[j]
					points[j] = temp
	return points

def pointSort(points):
	sortedArr = []
	y = None
	rev = False
	arrToSort = []
	for p in points:
		if y == None:
			y = p[1]
		if y == p[1]:
			arrToSort += [p]
		else:
			sortedArr += sortByX(arrToSort, rev)
			rev = not rev
			arrToSort = [p]
			y = p[1]
	sortedArr += sortByX(arrToSort, rev)
	return sortedArr

def lineintersects(shape,w):
    a = []
    maxI = 0;
    minI = 0;
    for z in range (len(shape)):
        if(shape[z][1] > maxI):
            maxI = shape[z][1];
        elif(shape[z][1] < minI):
            minI = shape[z][1];
    
    #count = 0;
    

    for i in range(int(maxI - w/2),int(minI),int(-w)):
        for j in range(len(shape)):
           
                if(shape[j][1] == shape[(j+1) % len(shape)][1]):
                    
                    if(i == shape[j][1]):
                    
                        a += [(shape[j][0],shape[j][1])]
                        a += [(shape[(j+1) % len(shape)][0],shape[(j+1) % len(shape)][1])]
                
                else:
                    x = None
                    if shape[j][0] == shape[(j+1) % len(shape)][0]:
                        x = shape[j][0]
                    else:
                        m = (shape[j][1]- shape[(j+1) % len(shape)][1])/(shape[j][0]-shape[(j+1) % len(shape)][0]);   
                        x = (i - shape[j][1] + m*shape[j][0])/m;
                    if( x >= min(shape[j][0],shape[(j+1) % len(shape)][0]) \
                    and x <= max(shape[j][0],shape[(j+1) % len(shape)][0]) \
                    and i >= min(shape[j][1],shape[(j+1) % len(shape)][1]) \
                    and i <= max(shape[j][1],shape[(j+1) % len(shape)][1])):
                       a += [(x,i)];
  
        

    a = pointSort(a)
    return a;
           
shape = [(0, 0), (0, 100), (300, 160), (300, 0)]
w = 20

points = lineintersects(shape, w)
i = 0
for p in points:
    i += 1
    print(str(i) + ":\t" + str(p) + "\n")
           
           

       
        

    

    
        
        
    
