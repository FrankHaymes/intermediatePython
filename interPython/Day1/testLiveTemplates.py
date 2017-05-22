import math

class Point:
    """
    Represents a point in 2-D geometric space
    """
    def __init__(self,x=0 , y =0):
        """
        Initalizes the position of a new point.
        If they are not specified, the points defaults to the origin
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the point to the origin in 2D space
        :return: Nothing
        """
        self.move(0,0)

    def move(self,x,y):
        """
        Move the point to the new location in 2D space
        :param x: x coordinate
        :param y: y coordinate
        :return:
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calulate the distances from this point to a second point pass as a parameter
        This function uses pythagorean Theorem to calculate
        the distance between the two points
        :param other_point: second point to calculate distance
        :return: The distance between two point(float)
        """
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)




def main():
    p1 = Point()
    print(p1.x, p1.y)
    p2 = Point(5,8)
    print(p2.x, p2.y)
    p2.reset()
    print(p2.x, p2.y)
    p2.move(9,10)
    print(p2.x,p2.y)
    p1 = Point(2,2)
    p2 = Point(4,4)
    print(p1.calculate_distance(p2))
    # test tool (assert)
    # program will exit if false
    assert(p1.calculate_distance(p2) == p2.calculate_distance(p1))

if __name__ == '__main__':
    main()
    exit(0)