class Point:
    '''
    Point oo the plane
    '''
    __x: int
    __y: int
    
    def __init__(self, x: int, y: int) -> None:
        '''
        :param x:
        :param y:
        '''
        # self.__x = x
        # self.__y = y 
        
        self.set__x(x)
        self.set__y(y)
    
    def get__x(self):
        return self.__x
    def set__x(self, x):
        self.__x = x
    
    def get__y(self):
        return self.__y
    def set__y(self, y):
        self.__y = y
        
    def __str__(self) -> str:
        return 'Point 2d (x: {0}, y: {1})'.format(self.get__x(), self.get__y())
        
    # return 'Point 2d (x: {0.get__x}, y: {0.get__y})'.format(self)
    
    
    def __eq__(self, other: "Point") -> bool:
        return self.__x == other.__x and self.__y == other.__y
    
    def __add__(self, other: "Point") -> float:
        return Point(self.__x + other.__x, self.__y + other.__y)
    
    def __sub__(self, other: "Point") -> float:
        return self.__class__(self.__x - other.__x, self.__y - other.__y)
    
    def distance(self) -> float:
        return (self.__x**2 + self.__y**2)**0.5


if __name__ == '__main__':
    # p = Point(2, 4.5)
    # print(dir(Point))
    # print(Point.__annotations__)
    # # print(p.__sizeof__)
    # # print(type(p))
    # print(p)
    # print(p.distance())
    p1 = Point(4, 5)
    p2 = Point(4, 5)
    # print(id(p1))
    # print(id(p2))
    print(p1.get__x(), p1.get__y())
    p2.set__y(77)
    print(p1 == p2)
    
    print(p1 + p2)
    
    