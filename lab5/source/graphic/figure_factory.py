from .point_3d import Point3D
from .figure import Figure

import math

class FigureFactory:
    @staticmethod
    def create_cube(center: Point3D = Point3D(0, 0, 0), side_length: float = 2) -> Figure:
        half_length = side_length / 2
        points = [
            Point3D(center.x - half_length, center.y - half_length, center.z - half_length),
            Point3D(center.x + half_length, center.y - half_length, center.z - half_length),
            Point3D(center.x + half_length, center.y + half_length, center.z - half_length),
            Point3D(center.x - half_length, center.y + half_length, center.z - half_length),
            Point3D(center.x - half_length, center.y - half_length, center.z + half_length),
            Point3D(center.x + half_length, center.y - half_length, center.z + half_length),
            Point3D(center.x + half_length, center.y + half_length, center.z + half_length),
            Point3D(center.x - half_length, center.y + half_length, center.z + half_length)
        ]
        return Figure(points)

    @staticmethod
    def create_pyramid(center: Point3D = Point3D(0, 0, 0), base_length: float = 2, height: float = 2) -> Figure:
        half_base = base_length / 2
        points = [
            Point3D(center.x - half_base, center.y - half_base, center.z - height / 2),
            Point3D(center.x + half_base, center.y - half_base, center.z - height / 2),
            Point3D(center.x + half_base, center.y + half_base, center.z - height / 2),
            Point3D(center.x - half_base, center.y + half_base, center.z - height / 2),
            Point3D(center.x, center.y, center.z + height / 2)
        ]
        return Figure(points)

    @staticmethod
    def create_sphere(center: Point3D = Point3D(0, 0, 0), radius: float = 1, segments=20, rings=20) -> Figure:
        points = []
        for s in range(segments):
            for r in range(rings):
                phi = math.pi * r / (rings - 1)
                theta = 2 * math.pi * s / (segments - 1)
                
                x = center.x + radius * math.sin(phi) * math.cos(theta)
                y = center.y + radius * math.sin(phi) * math.sin(theta)
                z = center.z + radius * math.cos(phi)

                points.append(Point3D(x, y, z))
        return Figure(points)