"""This module include Satellite class"""
from vpython import sphere, vector, pi


class Satellite():
    def __init__(self, diameter, distance_to_planet, rotation_period_in_hours, orbital_period_in_days, texture, mass,
                 planet):
        try:
            self.radius = diameter / 2
            self.distance_to_planet = distance_to_planet
            self.rotation_speed = 2 * pi / (rotation_period_in_hours * 3600)  # [rad/sec]
            self.orbit_speed = 2 * pi / (orbital_period_in_days * 3600 * 24)
            self.texture = texture
            self.mass = mass
            self.planet = planet  # TODO: THIS IS TEMP SOLUTION, MAKE BETTER ONE
            self.obj = sphere(radius=self.radius * self.planet.planet_scale,
                              pos=vector(self.planet.obj.pos.x - self.distance_to_planet * self.planet.distance_scale -
                                         self.planet.radius * self.planet.planet_scale -
                                         self.radius * self.planet.planet_scale,
                                         0, 0), texture=self.texture)
        except TypeError:
            print("TypeError: wrong arguments type!!")
        except ZeroDivisionError:
            print("ERROR: Rotation period and orbital period can't be zero")

    def update(self, time_scale):
        """This method of Satellite is empty because we can use time_scale from planet object that is already updated"""
        pass

    def rotate_axis(self):
        """Method that rotates satellite"""
        try:
            self.obj.rotate(angle=self.rotation_speed * self.planet.time_scale / self.planet.refresh_rate,
                            axis=vector(0, 1, 0))
        except ZeroDivisionError:
            print("ERROR: REFRESH_RATE is 0")
        except (AttributeError, TypeError):
            print("ERROR: wrong arguments type while initializing!!")

    def rotate_orbit(self):
        """Method that rotates satellite around a planet (including rotation around a star)"""
        try:
            self.obj.rotate(angle=self.planet.orbit_speed * self.planet.time_scale / self.planet.refresh_rate,
                            axis=vector(0, 1, 0), origin=self.planet.star.obj.pos)
            self.obj.rotate(angle=self.orbit_speed * self.planet.time_scale / self.planet.refresh_rate,
                            axis=vector(0, 1, 0), origin=self.planet.obj.pos)

        except ZeroDivisionError:
            print("ERROR: REFRESH_RATE is 0")
        except (AttributeError, TypeError):
            print("ERROR: wrong arguments type while initializing!!")
