import math
def convertdist(lat1,long1,lat2,long2):   
    long1 = math.radians(long1)
    lat1 = math.radians(lat1)
    long2 = math.radians(long2)
    lat2 = math.radians(lat2)

    a = (math.sin((lat2-lat1)/2)**2)+ math.cos(lat1)*math.cos(lat2)*(math.sin((long2-long1)/2)**2)
    d = 2*6371100*math.asin(math.sqrt(a))
    return d
def convertlatlong(X,Y,lat1,long1):
    d = sqrt(x**2+y**2)
    long2 = 2*asin(d/(sqrt(2*6371100)*cos(lat1)))+long1
    lat2 = 2*arcsin(d/(2*6371100))+lat1
    return [lat2,long2]

print(convertdist(38, 70, 39, 71))

print(convertdist(38.150417,-76.43212,38.14766,-76.428277))
    
