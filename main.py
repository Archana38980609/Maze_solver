from maze import Window,Point,Line

def main():

    win = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(200, 300)
    line = Line(p1, p2)
    win.draw_line(line)
    win.wait_for_close()

main()

