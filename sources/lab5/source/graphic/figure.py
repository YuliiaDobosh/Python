from .point_3d import Point3D
import numpy as np

class Figure:
    def __init__(self, points: list[Point3D]):
        self.points = points
        self.local_transform = np.eye(4)
        self.color = None
        self.symbol = None

    def copy(self):
        points_copy = [Point3D(p.x, p.y, p.z) for p in self.points]
        local_transform_copy = np.copy(self.local_transform)
        fig = Figure(points_copy)
        fig.local_transform = local_transform_copy
        fig.color = self.color
        fig.symbol = self.symbol
        return fig


    def translate(self, dx, dy, dz):
        """
        Update the local transformation matrix with a translation.
        """
        translation_matrix = np.array([
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1]
        ])
        
        # Multiply the current local transformation matrix with the translation matrix
        self.local_transform = np.dot(translation_matrix, self.local_transform)

    def get_transformed_point(self, point):
        """
        Transform a point using the local transformation matrix.
        """
        vec = np.array([point.x, point.y, point.z, 1])
        
        # Multiply the point's vector representation with the local transformation matrix
        transformed_vec = np.dot(self.local_transform, vec)
        
        return Point3D(
            x=transformed_vec[0] / transformed_vec[3],
            y=transformed_vec[1] / transformed_vec[3],
            z=transformed_vec[2] / transformed_vec[3]
        )

    def set_color(self, color: str):
        self.color = color

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def __repr__(self) -> str:
        return f"[{','.join(self.points)}]"