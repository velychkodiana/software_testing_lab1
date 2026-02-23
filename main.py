# main.py

from errors import LabInputError
from input_validation import read_variant_inputs
from line_models import line_from_two_points, line_from_intercepts, line_from_slope_intercept
from line_relations import analyze_three_lines


def main() -> None:
    print("Лабораторна робота №1")
    print("Варіант: Величко Діана (2,4,5)")
    print("Python / PyCharm\n")

    try:
        p, inter, si = read_variant_inputs()

        l1 = line_from_two_points(p.x1, p.y1, p.x2, p.y2)
        l2 = line_from_intercepts(inter.a, inter.b)
        l3 = line_from_slope_intercept(si.k, si.b)

        message, _points = analyze_three_lines(l1, l2, l3)

        print("\n=== Результат ===")
        print(message)

    except LabInputError as e:
        print("\n=== Помилка введення ===")
        print(str(e))
    except Exception as e:
        # На випадок непередбаченого
        print("\n=== Непередбачена помилка ===")
        print(f"Помилка: {e}; Як виправити: перевірте реалізацію або зверніться до викладача.")


if __name__ == "__main__":
    main()