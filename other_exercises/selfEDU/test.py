class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    pass


pt = Point3D(10, 20)
pt.x
pt.z = 25
pt.__dict__