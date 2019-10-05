from math import sqrt


class PointError(Exception):
    a= 0
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y
    # Possibly define other methods
    

class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    
    def __init__(self, *, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.p_1x = self.point_1.x
        self.p_2x = self.point_2.x
        self.p_3x = self.point_3.x
        self.p_1y = self.point_1.y
        self.p_2y = self.point_2.y
        self.p_3y = self.point_3.y
        self.a = sqrt((self.p_2x-self.p_3x)**2+(self.p_2y-self.p_3y)**2)
        self.b = sqrt((self.p_3x-self.p_1x)**2+(self.p_3y-self.p_1y)**2)
        self.c = sqrt((self.p_1x-self.p_2x)**2+(self.p_1y-self.p_2y)**2)
        if (self.a + self.b - self.c) * (self.a + self.c - self.b) * (self.b + self.c - self.a) > 0:
            self.compute_perimeter()
            self.compute_area()
        else:
            raise TriangleError('Incorrect input, triangle not created.')
        
    def compute_perimeter(self):
        self.perimeter = self.a+self.b+self.c
        self.halfp = self.perimeter/2
            
        
    def compute_area(self):
        self.area = sqrt(self.halfp*(self.halfp-self.a)*(self.halfp-self.b)*(self.halfp-self.c))   
        # Replace pass above with your code
    	
    def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
        if point_1 is not None:
            self.point_1 = point_1
            self.p_1x = self.point_1.x
            self.p_1y = self.point_1.y
            self.a = sqrt((self.p_2x-self.p_3x)**2+(self.p_2y-self.p_3y)**2)
            self.b = sqrt((self.p_3x-self.p_1x)**2+(self.p_3y-self.p_1y)**2)
            self.c = sqrt((self.p_1x-self.p_2x)**2+(self.p_1y-self.p_2y)**2)
        if point_2 is not None:
            self.point_2 = point_2
            self.p_2x = self.point_2.x
            self.p_2y = self.point_2.y
            self.a = sqrt((self.p_2x-self.p_3x)**2+(self.p_2y-self.p_3y)**2)
            self.b = sqrt((self.p_3x-self.p_1x)**2+(self.p_3y-self.p_1y)**2)
            self.c = sqrt((self.p_1x-self.p_2x)**2+(self.p_1y-self.p_2y)**2)
        if point_3 is not None:
            self.point_3 = point_3
            self.p_3x = self.point_3.x
            self.p_3y = self.point_3.y
            self.a = sqrt((self.p_2x-self.p_3x)**2+(self.p_2y-self.p_3y)**2)
            self.b = sqrt((self.p_3x-self.p_1x)**2+(self.p_3y-self.p_1y)**2)
            self.c = sqrt((self.p_1x-self.p_2x)**2+(self.p_1y-self.p_2y)**2)
        if (self.a + self.b - self.c) * (self.a + self.c - self.b) * (self.b + self.c - self.a) > 0:
            self.compute_perimeter()
            self.compute_area()
        else:
            print ('Incorrect input, triangle not modified.')
            
        # Replace pass above with your code

    # Possibly define other methods
        