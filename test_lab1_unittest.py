import unittest

from line_models import (
    line_from_two_points,
    line_from_intercepts,
    line_from_slope_intercept,
)
from line_relations import analyze_three_lines


class TestLab1(unittest.TestCase):
    # --------- P1: coincident exists ----------
    def test_p1_t1_coincident(self):
        l1 = line_from_two_points(0, 3, 1, 5)      # y=2x+3
        l2 = line_from_intercepts(1, 1)            # x+y=1
        l3 = line_from_slope_intercept(2, 3)       # y=2x+3
        msg, _ = analyze_three_lines(l1, l2, l3)
        self.assertEqual(msg, "Прямі співпадають")

    def test_p1_t3_horizontal_coincident(self):
        l1 = line_from_two_points(0, 10, 5, 10)    # y=10
        l2 = line_from_intercepts(1, 1)
        l3 = line_from_slope_intercept(0, 10)      # y=10
        msg, _ = analyze_three_lines(l1, l2, l3)
        self.assertEqual(msg, "Прямі співпадають")

    # --------- P2: no intersections ----------
    def test_p2_t1_no_intersections(self):
        l1 = line_from_two_points(0, 1, 1, 2)      # y=x+1
        l2 = line_from_intercepts(1, -1)           # y=x-1
        l3 = line_from_slope_intercept(1, 3)       # y=x+3
        msg, _ = analyze_three_lines(l1, l2, l3)
        self.assertEqual(msg, "Прямі не перетинаються")

    # --------- P3: single intersection point ----------
    def test_p3_t1_single_point(self):
        l1 = line_from_two_points(1, 1, 2, 2)  # y=x
        l2 = line_from_intercepts(2, 2)  # x+y=2
        l3 = line_from_slope_intercept(2, -1)  # y=2x-1 (проходить через (1,1), b≠0)
        msg, pts = analyze_three_lines(l1, l2, l3)
        self.assertTrue(msg.startswith("Єдина точка перетину"))
        self.assertEqual(len(pts), 1)

    # --------- P4: two points ----------
    def test_p4_t1_two_points(self):
        l1 = line_from_two_points(0, 0, 1, 0)      # y=0
        l2 = line_from_intercepts(1, 1)            # x+y=1
        l3 = line_from_slope_intercept(0, 2)       # y=2
        msg, pts = analyze_three_lines(l1, l2, l3)
        self.assertTrue(msg.startswith("Дві точки перетину"))
        self.assertEqual(len(pts), 2)

    # --------- P5: three points ----------
    def test_p5_t1_three_points(self):
        l1 = line_from_two_points(10, 10, 20, 10)  # y=10
        l2 = line_from_intercepts(1, 1)            # x+y=1
        l3 = line_from_slope_intercept(2, 3)       # y=2x+3
        msg, pts = analyze_three_lines(l1, l2, l3)
        self.assertTrue(msg.startswith("Три точки перетину"))
        self.assertEqual(len(pts), 3)


if __name__ == "__main__":
    unittest.main()