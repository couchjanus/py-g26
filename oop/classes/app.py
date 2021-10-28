class Point:
    '''
    Point oo the plane
    '''
    x: int
    y: int
    
    def __init__(self, x: int, y: int) -> None:
        '''
        :param x:
        :param y:
        '''
        self.x = x
        self.y = y 
    
    def __str__(self) -> str:
        return 'Point 2d (x: {0.x}, y: {0.y})'.format(self)
    
    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other: "Point") -> float:
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> float:
        return self.__class__(self.x - other.x, self.y - other.y)
    
    def distance(self) -> float:
        return (self.x**2 + self.y**2)**0.5


if __name__ == '__main__':
    # p = Point(2, 4.5)
    print(dir(Point))
    print(Point.__annotations__)
    # # print(p.__sizeof__)
    # # print(type(p))
    # print(p)
    # print(p.distance())
    p1 = Point(4, 5)
    p2 = Point(4, 5)
    print(id(p1))
    print(id(p2))
    print(p1.__annotations__)
    print(p1 == p2)
    
    print(p1 + p2)
    
    