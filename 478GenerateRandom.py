"""
Given the radius and x-y positions of the center of a circle,
write a function randPoint which generates a uniform random point in the circle.

Note:
input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
"""

from typing import List
from random import uniform, random
from math import pi, sin, cos
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        # Cartesian method
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = uniform(self.x_min, self.x_max)
            y = uniform(self.y_min, self.y_max)
            if (x - self.x_center) ** 2 + (y - self.y_center) ** 2 <= self.radius ** 2:
                return [x, y]


class Solution2:
    # Polar coordinate
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        length = random()**0.5 * self.radius
        deg = random() * 2 * pi
        x = self.x_center + length * cos(deg)
        y = self.y_center + length * sin(deg)
        return [x, y]


# Your Solution object will be instantiated and called as such:
radius, x_center, y_center = 1,0,0
# radius, x_center, y_center = 10,5,-7.5
obj = Solution2(radius, x_center, y_center)
print(obj.randPoint())
