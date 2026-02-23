# line_models.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

EPS = 1e-8


def is_zero(z: float) -> bool:
    return abs(z) <= EPS


@dataclass(frozen=True)
class LineABC:
    A: float
    B: float
    C: float

    def as_tuple(self) -> Tuple[float, float, float]:
        return self.A, self.B, self.C


def line_from_two_points(x1: int, y1: int, x2: int, y2: int) -> LineABC:
    """
    Через 2 точки.
    Стандартна формула:
      A = y1 - y2
      B = x2 - x1
      C = x1*y2 - x2*y1
    """
    A = float(y1 - y2)
    B = float(x2 - x1)
    C = float(x1 * y2 - x2 * y1)
    return LineABC(A, B, C)


def line_from_intercepts(a: int, b: int) -> LineABC:
    """
    У відрізках: x/a + y/b = 1
    Приводимо:
      (b)x + (a)y - (a*b) = 0
      A = b, B = a, C = -a*b
    """
    A = float(b)
    B = float(a)
    C = float(-a * b)
    return LineABC(A, B, C)


def line_from_slope_intercept(k: int, b: int) -> LineABC:
    """
    З кутовим коефіцієнтом: y = kx + b
    -> kx - y + b = 0
    A = k, B = -1, C = b
    """
    A = float(k)
    B = -1.0
    C = float(b)
    return LineABC(A, B, C)