class Coordinate:
    """A coordinate made up of a x and y value."""

    def __init__(self, x: int, y: int):
        """Set the values of x and y."""
        self.x = x
        self.y = y

    def distance(self, other: tuple):
        """Returns the distance between two points."""
        x_sqr = (self.x - other.x) ** 2
        y_sqr = (self.y - other.y) ** 2
        return (x_sqr + y_sqr) ** 0.5


point_1 = Coordinate(3, 5)
point_2 = Coordinate(2, 9)
print(point_1.x)
print(point_1.y)

distance = point_1.distance(point_2)
print(f"{distance:.2f}")
