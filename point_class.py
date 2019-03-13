class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "("+self.x+","+self.y+")"

    #return "{}, {}".format(self.x, self.y)


    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)

    def __sub__(self, point):
        return self + -point

    def __lt__(self,other):
        if(self.x < other.x):
            return True
        elif(self.x > other.x):
            return False
        else:
            if(self.y < other.y):
                return True
            elif(self.y > other.y):
                return False
            else:
                return False

    def __le__(self,other):
        if(self.x < other.x):
            return True
        elif(self.x > other.x):
            return False
        else:
            if(self.y < other.y):
                return True
            elif(self.y > other.y):
                return False
            else:
                return True

    def __gt__(self,other):
        if(self.x > other.x):
            return True
        elif(self.x < other.x):
            return False
        else:
            if(self.y > other.y):
                return True
            elif(self.y < other.y):
                return False
            else:
                return False

    def __ge__(self,other):
        if(self.x > other.x):
            return True
        elif(self.x < other.x):
            return False
        else:
            if(self.y > other.y):
                return True
            elif(self.y < other.y):
                return False
            else:
                return True

    def __eq__(self, other):
        if((self.x == other.x) and (self.y == other.y)):
            return True
        else:
            return False

    def __ne__(self, other):
        if((self.x == other.x) and (self.y == other.y)):
            return False
        else:
            return True
