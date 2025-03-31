from maze import Line, Point

class Cell:
    def __init__(self,x1,y1,x2,y2,win = None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        if self._win is None:
            return

        if self.has_left_wall:
            left_wall = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            left_wall.draw(self._win)


        if self.has_top_wall:
            top_wall = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            top_wall.draw(self._win)


        if self.has_right_wall:
            right_wall = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            right_wall.draw(self._win)


        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            bottom_wall.draw(self._win)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        centre_x1 = (self._x1 + self._x2)//2
        centre_y1 = (self._y1 + self._y2)//2

        centre_x2 = (to_cell._x1 + to_cell._x2)//2
        centre_y2 = (to_cell._y1 + to_cell._y2)//2

        color = "gray" if undo else "red"

        line = Line(Point(centre_x1, centre_y1), Point(centre_x2, centre_y2))
        line.draw(self._win, color)