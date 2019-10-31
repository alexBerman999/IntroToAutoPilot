import math
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
                
                    m = (shape[j][1]- shape[(j+1) % len(shape)][1])/(shape[j][0]-shape[(j+1) % len(shape)][0]);
       
                    x = (i - shape[j][1] + m*shape[j][0])/m;
                    if( x > min(shape[j][0],shape[(j+1) % len(shape)][0]) and x < max(shape[j][0],shape[(j+1) % len(shape)][0])):
                       a += [(x,i)];
  
        


    return a;
           
shape = [(0, 0), (5, 8), (10, 0)]
w = 2

points = lineintersects(shape, w)
i = 0
for p in points:
    i += 1
    print(str(i) + ":\t" + str(p) + "\n")
           
           

       
        

    

    
        
        
    
