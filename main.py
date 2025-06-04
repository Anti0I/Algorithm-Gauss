
from gauss import gauss_elimination
from input import get_user_input

def main():
        A, b = get_user_input()
        solution = gauss_elimination(A, b)
        print("\nRozwiązanie układu:")
        for i, x in enumerate(solution):
            print(f"x{i} = {x:.3f}")


if __name__ == "__main__":
    main()
