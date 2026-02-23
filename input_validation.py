# input_validation.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple

from errors import RangeError, FormatError, GeometryError

MIN_V = -113
MAX_V = 113


def _parse_int(raw: str, field_name: str) -> int:
    raw = raw.strip()
    try:
        # Забороняємо "12.3" та інше — має бути саме ціле
        if raw.startswith("+"):
            raw = raw[1:]
        value = int(raw)
        return value
    except ValueError as e:
        raise FormatError(
            f"Помилка: поле '{field_name}' має бути цілим числом; "
            f"Як виправити: введіть ціле число без дробової частини (наприклад 0, -5, 12)."
        ) from e


def _check_range(value: int, field_name: str) -> int:
    if not (MIN_V <= value <= MAX_V):
        raise RangeError(
            f"Помилка: '{field_name}' поза допустимим діапазоном [{MIN_V}; {MAX_V}]; "
            f"Як виправити: введіть значення в межах [{MIN_V}; {MAX_V}]."
        )
    return value


def read_int(field_name: str) -> int:
    raw = input(f"Введіть {field_name}: ")
    value = _parse_int(raw, field_name)
    return _check_range(value, field_name)


@dataclass(frozen=True)
class TwoPointsInput:
    x1: int
    y1: int
    x2: int
    y2: int

    def validate(self) -> None:
        # точки не співпадають: (x1-x2)^2 + (y1-y2)^2 != 0
        if self.x1 == self.x2 and self.y1 == self.y2:
            raise GeometryError(
                "Помилка: для прямої через 2 точки задані однакові точки; "
                "Як виправити: введіть дві різні точки (x1,y1) та (x2,y2)."
            )


@dataclass(frozen=True)
class InterceptsInput:
    a: int
    b: int

    def validate(self) -> None:
        if self.a == 0 or self.b == 0:
            raise GeometryError(
                "Помилка: для рівняння у відрізках потрібно a ≠ 0 та b ≠ 0; "
                "Як виправити: введіть ненульові a і b."
            )


@dataclass(frozen=True)
class SlopeInterceptInput:
    k: int
    b: int

    def validate(self) -> None:
        if self.b == 0:
            raise GeometryError(
                "Помилка: для рівняння з кутовим коефіцієнтом потрібно b ≠ 0; "
                "Як виправити: введіть ненульове b."
            )


def read_variant_inputs() -> Tuple[TwoPointsInput, InterceptsInput, SlopeInterceptInput]:
    """
    Варіант Величко Діана: 2,4,5
    (2) через 2 точки
    (4) у відрізках
    (5) з кутовим коефіцієнтом (k,b), b != 0
    """
    print("\n=== Пряма №1: через 2 точки (x1,y1), (x2,y2) ===")
    x1 = read_int("x1")
    y1 = read_int("y1")
    x2 = read_int("x2")
    y2 = read_int("y2")
    p = TwoPointsInput(x1, y1, x2, y2)
    p.validate()

    print("\n=== Пряма №2: у відрізках (a, b) ===")
    a = read_int("a")
    b = read_int("b")
    inter = InterceptsInput(a, b)
    inter.validate()

    print("\n=== Пряма №3: з кутовим коефіцієнтом (k, b), b≠0 ===")
    k = read_int("k")
    b2 = read_int("b")
    si = SlopeInterceptInput(k, b2)
    si.validate()

    return p, inter, si