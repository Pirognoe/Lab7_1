import math


class Sphere(object):
    # radius = 1.0
    # x = 0
    # y = 0
    # z = 0

    def __init__(self, radius, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):  # Calculate the volume
        volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return volume

    def get_square(self):
        square = 4 * math.pi * math.pow(self.radius, 2)
        return square

    def get_radius(self):
        return self.radius

    def get_center(self):
        coordinats = tuple((self.x, self.y, self.z))
        return coordinats

    def set_radius(self, r):
        self.radius = r
        return self

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        delta_x = self.x - x
        delta_y = self.y - y
        delta_z = self.z - z
        distance_center_point = math.pow(delta_x, 2) + math.pow(delta_y, 2) + math.pow(delta_z, 2)
        if distance_center_point <= math.pow(self.radius, 2):
            return True
        else:
            return False

s0 = Sphere(0.5)

print("Proba")
print(s0.get_center())  # (0.0, 0.0, 0.0)
print(s0.get_volume(), 0.523598775598, "Works")
print(s0.get_square(), "Works")
print (s0.is_point_inside(0, -1.5, 0), "False") #
print(s0.get_radius(), "Works")
s0.set_radius(1.6)
print (s0.is_point_inside(0, -1.5, 0), "True") #
print(s0.get_radius(), "__", s0.get_volume(), 0.523598775598)  # 1.6
print(s0.get_square())
s0.set_center(5.1, -2, 1.1)
print(s0.get_center())  # (0.0, 0.0, 0.0)
print("Finish")
