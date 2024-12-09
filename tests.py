import unittest
from maze import Maze

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

    def test_maze_small(self):
        num_cols = 1
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_larger_amount(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


    def test_break_entrance_and_exit(self):
        num_cols = 9
        num_rows = 10
        m1 = Maze(0 , 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].top_wall, False
        )
        self.assertEqual(
            m1._cells[m1.num_cols-1][m1.num_rows-1].bottom_wall, False
        )

    def test_maze_set_to_not_visited_after_build(self):
        num_cols = 9
        num_rows = 10
        m1 = Maze(0 , 0, num_rows, num_cols, 10, 10)
        all_false = True
        for i in range(0, m1.num_cols):
            for j in range(0, m1.num_rows):
                if m1._cells[i][j].visited == True:
                    all_false = False
        self.assertEqual(True, all_false)

if __name__ == "__main__":
    unittest.main()