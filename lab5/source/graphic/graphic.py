from .point_2d import Point2D
from .point_3d import Point3D
from .figure import Figure
from .color import Color

import numpy as np

import curses

class Graphic():
    def __init__(self) -> None:
        super().__init__()
        self.window = None
        self.is_init = False
        self.figures: list[Figure] = []

        self.camera_position: Point3D = Point3D(0, 2, 5)
        self.camera_look_at: Point3D = Point3D(0, 0, 0)
        self.camera_near: int = 0.5
        self.camera_far: int = 100

    @property
    def last_figure(self) -> Figure:
        l = len(self.figures)
        if l <= 0:
            return
        return self.figures[l - 1]

    @property
    def final_transform(self):
        view = self.look_at(np.array([self.camera_position.x, self.camera_position.y, self.camera_position.z]),
                            np.array([self.camera_look_at.x, self.camera_look_at.y, self.camera_look_at.z]),
                            np.array([0, 1, 0]))
        projection = self.perspective_projection(90, self.width/self.height, self.camera_near, self.camera_far)

        final_transform = projection @ view

        return final_transform

    def add_figure(self, figure: Figure) -> None:
        self.figures.append(figure)

    
    def __draw_point(self, point: Point2D, symbol: str, color) -> None:
        if 0 <= point.x < self.width and 0 <= point.y < self.height:
            if point.x != self.width - 1 and point.y != self.height - 1: 
                self.window.addch(point.y, point.x, symbol, curses.color_pair(color.value))

    def __render_figure(self, figure: Figure, symbol: str, color) -> None:
        for point in figure.points:
            
            # Step 1: Transform the point using the figure's local transformation matrix
            locally_transformed_point = figure.get_transformed_point(point)
            
            # Step 2: Convert the locally transformed point to homogeneous coordinates
            vec = np.array([locally_transformed_point.x, locally_transformed_point.y, locally_transformed_point.z, 1])
            
            # Step 3: Apply the final transformation
            transformed_vec = self.final_transform.dot(vec)
            
            # Step 4: Convert back to Cartesian coordinates
            transformed_point = Point2D(
                x=transformed_vec[0] / transformed_vec[3],
                y=transformed_vec[1] / transformed_vec[3]
            )
    
            # Step 5: Denormalize the coordinates for rendering
            denormalized_point = self.denormalize_coordinates(transformed_point, self.width, self.height)
            
            # Step 6: Draw the point
            self.__draw_point(denormalized_point, symbol, color)

    def render_figures(self) -> None:
        for figure in self.figures:
            self.__render_figure(figure, figure.symbol, figure.color)

    def set_window(self, window):
        self.window = window
        self.init()
        self.is_init = True

    def init(self):
        if not self.is_init:    
            curses.start_color()
            
            curses.init_pair(Color.RED.value, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(Color.GREEN.value, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(Color.BLUE.value, curses.COLOR_BLUE, curses.COLOR_BLACK)

            curses.curs_set(0)
            
            self.height, self.width = self.window.getmaxyx()
            self.window.nodelay(0)

    @staticmethod
    def translation_matrix(tx, ty, tz):
        return np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_matrix_x(angle):
        c = np.cos(angle)
        s = np.sin(angle)
        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_matrix_y(angle):
        c = np.cos(angle)
        s = np.sin(angle)
        return np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def rotation_matrix_z(angle):
        c = np.cos(angle)
        s = np.sin(angle)
        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def scale_matrix(sx, sy, sz):
        return np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def look_at(camera_position, target, up_vector):
        zaxis = (camera_position - target) / np.linalg.norm(camera_position - target)
        xaxis = np.cross(up_vector, zaxis)
        yaxis = np.cross(zaxis, xaxis)

        return np.array([
            [xaxis[0], xaxis[1], xaxis[2], -np.dot(xaxis, camera_position)],
            [yaxis[0], yaxis[1], yaxis[2], -np.dot(yaxis, camera_position)],
            [zaxis[0], zaxis[1], zaxis[2], -np.dot(zaxis, camera_position)],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def perspective_projection(fov, aspect_ratio, near, far):
        t = np.tan(np.radians(fov) / 2) * near
        r = t * aspect_ratio

        return np.array([
            [near / r, 0, 0, 0],
            [0, near / t, 0, 0],
            [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
            [0, 0, -1, 0]
        ])

    def denormalize_coordinates(self, normalized_point: Point2D, width, height, pixel_aspect=1.0) -> Point2D:
        """Денормалізує координати з діапазону [-1, 1] до [width, height].

        :param normalized_x: Нормалізована x-координата.
        :param normalized_y: Нормалізована y-координата.
        :param width: Ширина екрану.
        :param height: Висота екрану.
        :param pixel_aspect: Aspect ratio пікселів.
        :return: Денормалізовані координати (x, y).
        """
        
        screen_aspect = 1
        
        # Денормалізація координат до [0, 1]
        denormalized_x = 0.5 * (normalized_point.x + 1) * width
        denormalized_y = 0.5 * (normalized_point.y + 1) * height

        # Корекція координат за aspect ratio екрану і пікселів
        if screen_aspect > pixel_aspect:
            corrected_x = denormalized_x * pixel_aspect / screen_aspect
            corrected_y = denormalized_y
        else:
            corrected_x = denormalized_x
            corrected_y = denormalized_y * screen_aspect / pixel_aspect
        
        return Point2D(int(corrected_x), int(corrected_y))