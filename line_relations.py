# line_relations.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple, List

from line_models import LineABC, is_zero, EPS


Point = Tuple[float, float]


@dataclass(frozen=True)
class PairResult:
    kind: str  # "coincident" | "parallel" | "intersect"
    point: Optional[Point] = None


def are_coincident(l1: LineABC, l2: LineABC) -> bool:
    """
    Перевірка співпадіння:
    A1:B1:C1 пропорційні A2:B2:C2.
    Робимо без ділення (щоб не падати на нулі):
      A1*B2 == A2*B1
      A1*C2 == A2*C1
      B1*C2 == B2*C1
    Досить двох незалежних, але зробимо три з EPS.
    """
    A1, B1, C1 = l1.as_tuple()
    A2, B2, C2 = l2.as_tuple()

    return (
        is_zero(A1 * B2 - A2 * B1)
        and is_zero(A1 * C2 - A2 * C1)
        and is_zero(B1 * C2 - B2 * C1)
    )


def pair_relation(l1: LineABC, l2: LineABC) -> PairResult:
    """
    Повертає:
      - coincident
      - parallel
      - intersect(point)
    """
    A1, B1, C1 = l1.as_tuple()
    A2, B2, C2 = l2.as_tuple()

    det = A1 * B2 - A2 * B1

    if is_zero(det):
        if are_coincident(l1, l2):
            return PairResult("coincident", None)
        return PairResult("parallel", None)

    # Формули Крамера для:
    # A1 x + B1 y + C1 = 0
    # A2 x + B2 y + C2 = 0
    x = (B1 * C2 - B2 * C1) / det
    y = (C1 * A2 - C2 * A1) / det
    return PairResult("intersect", (x, y))


def _points_equal(p1: Point, p2: Point) -> bool:
    return abs(p1[0] - p2[0]) <= EPS and abs(p1[1] - p2[1]) <= EPS


def unique_points(points: List[Point]) -> List[Point]:
    uniq: List[Point] = []
    for p in points:
        if not any(_points_equal(p, q) for q in uniq):
            uniq.append(p)
    return uniq


def analyze_three_lines(l1: LineABC, l2: LineABC, l3: LineABC) -> Tuple[str, List[Point]]:
    """
    Повертає (message, points)
    message має відповідати одному з 5 варіантів виводу.
    """

    r12 = pair_relation(l1, l2)
    r13 = pair_relation(l1, l3)
    r23 = pair_relation(l2, l3)

    # Відповідність вимогам:
    # якщо є хоча б одна пара, що співпадає => повідомлення "Прямі співпадають"
    # (програма має видати ОДНЕ з повідомлень зі списку)
    if r12.kind == "coincident" or r13.kind == "coincident" or r23.kind == "coincident":
        return "Прямі співпадають", []

    # Немає співпадінь. Зберемо точки перетину, де вони є:
    pts: List[Point] = []
    for r in (r12, r13, r23):
        if r.kind == "intersect" and r.point is not None:
            pts.append(r.point)

    pts = unique_points(pts)

    if len(pts) == 0:
        return "Прямі не перетинаються", []

    if len(pts) == 1:
        x0, y0 = pts[0]
        return f"Єдина точка перетину прямих (x0, y0), x0={x0}, y0={y0}", pts

    if len(pts) == 2:
        (x1, y1), (x2, y2) = pts
        return f"Дві точки перетину прямих (x1, y1)=({x1}, {y1}), (x2, y2)=({x2}, {y2})", pts

    (x1, y1), (x2, y2), (x3, y3) = pts[:3]
    return (
        "Три точки перетину прямих "
        f"(x1, y1)=({x1}, {y1}), (x2, y2)=({x2}, {y2}), (x3, y3)=({x3}, {y3})",
        pts,
    )