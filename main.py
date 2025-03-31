from maze import Window,Point,Line
from cell import Cell
def main():

    win = Window(800, 600)
    
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.has_left_wall = False
    cell1.draw()

    cell2 = Cell(150, 50, 200, 100, win)
    cell2.has_top_wall = False
    cell2.draw()

    cell3 = Cell(350, 50, 400, 100, win)
    cell3.has_right_wall = False
    cell3.draw()

    cell4 = Cell(450, 50, 500, 100, win)
    cell4.has_bottom_wall = False
    cell4.draw()
    

    win.wait_for_close()

main()

