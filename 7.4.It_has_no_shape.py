# Omer Gertler

from random import randint


class Rectangle:
    """ Create rectangles. A rectangle defined by start0point and end-point.

    Args:
        start_point (tuple (<int>, <int>)): upper-left point.
        end_point (tuple (<int>, <int>)): down-right point.

    Attributes:
        start_point (tuple (<int>, <int>)): upper-left point.
        end_point (tuple (<int>, <int>)): down-right point.
    """

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f'start point: {self.start_point}, end point: {self.end_point}'

    def get_surface(self):
        """ Return the surface of the rectangle """
        height = self.end_point[1] - self.start_point[1]
        width = self.end_point[0] - self.start_point[0]
        return height * width

    def get_perimeter(self):
        """ Return the perimeter of the rectangle """
        height = self.end_point[1] - self.start_point[1]
        width = self.end_point[0] - self.start_point[0]
        return (height + width) * 2

    def randomize_start_point(self):
        """ Choose random int values for the start point (x, y)"""
        x = randint(1, 100)
        y = randint(1, 100)
        self.start_point = (x, y)

    def randomize_end_point(self):
        """ Choose random int values for the end point (x, y)"""
        x = randint(1, 100)
        y = randint(1, 100)
        self.end_point = (x, y)

    def filter_by_size(self, rectangles, threshold):
        """ Return list of the rectangles with surface at least the threshold.

        :param list rectangles: List of Rectangle rectangles.
        :param int threshold: The minimum surface area.
        :return: List of the rectangles.
        """
        return [rec for rec in rectangles if rec.get_surface() >= threshold]

    def filter_by_perimeter(self, rectangles, threshold):
        """ Return list of the rectangles with perimeter at least the threshold.

        :param list rectangles: List of Rectangle rectangles.
        :param int threshold: The minimum perimeter value.
        :return: List of the rectangles.
        """
        return [rec for rec in rectangles if rec.get_perimeter() >= threshold]

    def rand_rects(self):
        """ Crate and print list of 1-50 Rectangle rectangles with random end and start points. """
        rectangles = []
        num = randint(1, 50)
        for i in range(num):
            rectangles.append(Rectangle(self.randomize_start_point(), self.randomize_end_point()))
        for rec in rectangles:
            if rec.get_surface() > 900 and rec.get_perimeter() > 30:
                print(rec)
