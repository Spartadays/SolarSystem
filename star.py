"""This module include Star class"""
from vpython import sphere, vector, pi, local_light, color


class Star:
    def __init__(self, diameter, rotation_period_in_hours, texture, mass, time_scale, refresh_rate, sun_scale):
        try:
            self.radius = diameter / 2
            self.rotation_speed = 2 * pi / (rotation_period_in_hours * 3600)  # [rad/sec]
            self.texture = texture
            self.mass = mass
            self.time_scale = time_scale
            self.refresh_rate = refresh_rate
            self.sun_scale = sun_scale
            self.obj = sphere(radius=self.radius * self.sun_scale, pos=vector(0, 0, 0), texture=self.texture,
                              emissive=True, opacity=1)
            self.light = None
        except TypeError:
            print("TypeError: wrong arguments type!!")
        except ZeroDivisionError:
            print("ERROR: Rotation period can't be zero")

    def update(self, time_scale):
        """This method is used to update time_scale which can be changed from outside this class"""
        self.time_scale = time_scale

    def light_on(self):
        self.light = local_light(pos=self.obj.pos, color=color.white)

    def rotate_axis(self):
        """Method that rotates star"""
        try:
            self.obj.rotate(angle=self.rotation_speed * self.time_scale / self.refresh_rate, axis=vector(0, 1, 0))
        except ZeroDivisionError:
            print("ERROR: REFRESH_RATE is 0")
        except (AttributeError, TypeError):
            print("ERROR: wrong arguments type while initializing!!")
