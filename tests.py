import unittest
from maze_class import Maze
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 5
        num_rows = 5
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 25
        num_rows = 30
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        maze = Maze(0, 0, 3, 3, 10, 10)
    
        entrance_cell = maze._cells[0][0]
        exit_cell = maze._cells[2][2]
        entrance_cell.has_top_wall = True
        exit_cell.has_bottom_wall = True
    
        self.assertTrue(entrance_cell.has_top_wall)
        self.assertTrue(exit_cell.has_bottom_wall)

        maze._break_entrance_and_exit()
    
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()