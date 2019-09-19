from random import randint

class Map:

    def __init__(self, width, height, obsts, wps):
        self.X_RANGE = (0, width)
        self.Y_RANGE = (0, height)
        self.SIZE_RANGE = (9, 92)
        self.obstacles = []
        self.waypoints = []
        self.generateObstacles(obsts)
        self.generateWaypoints(wps)

    def generateObstacles(self, amt):
        for i in range(amt):
            #X, Y, radius
            self.obstacles += [(randint(*self.X_RANGE), randint(*self.Y_RANGE), randint(*self.SIZE_RANGE))]

    def generateWaypoints(self, amt):
        for i in range(amt):
            wp = (randint(*self.X_RANGE), randint(*self.Y_RANGE))
            while self.collides(wp):
                wp = (randint(*self.X_RANGE), randint(*self.Y_RANGE))
            self.waypoints += [wp]

    def distance(self, point1, point2):
        return (((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)) ** (1/2)

    def collides(self, point, buffer=0):
        for obst in self.obstacles:
            dist = (((point[0] - obst[0]) ** 2) + ((point[1] - obst[1]) ** 2)) ** (1/2)
            if dist < (obst[2] + buffer):
                return True
        return False

    #def collidesLine(self, point1, point2, buffer=0):
        #a = (point1[1] - point2[1])
        #b = (point2[0] - point1[0])
        #c = ((point1[0] * point2[1]) - (point2[0] * point1[1]))
        #for obst in self.obstacles:
        #    dist = abs((a * obst[0]) + (b * obst[1]) + c) / (((a * a) + (b * b)) ** (1/2))
        #    if dist < obst[2]:
        #        return True
        #return False
        #for obst in self.obstacles:
        #    a_pt = (point1[0] - obst[0], point1[1] - obst[1])
        #    b_pt = (point2[0] - obst[0], point2[1] - obst[1])
        #    print(a_pt)
        #    print(b_pt)
        #    c = (a_pt[0] ** 2) + (a_pt[1] ** 2) - ((obst[2] + buffer) ** 2)
        #    b = 2 * (a_pt[0] * (b_pt[0] - a_pt[0]) + a_pt[1]*(b_pt[1] - a_pt[1]))
        #    a = ((b_pt[0] - a_pt[0]) ** 2) + ((b_pt[1] - a_pt[1]) ** 2)
        #    disc = (b ** 2) - (4 * a * c)
        #    if disc <= 0:
        #        print("Here")
        #        return False
        #    sqrtdisc = disc ** (1/2)
        #    t1 = (-b + sqrtdisc) / (2 * a)
        #    t2 = (-b - sqrtdisc) / (2 * a)
        #    if (0 < t1 and t1 < 1) or (0 < t2 and t2 < 1):
        #        return True
        #return False
