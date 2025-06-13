from gauss import gauss
from input import get_user_input


def calculate():
    A, b = get_user_input()
    solution = gauss(A, b)
    print("\nRozwiazanie ukladu:")
    for i, x in enumerate(solution):
        print(f"x{i} = {x:.3f}")


if __name__ == "__main__":
    calculate()
