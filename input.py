def get_user_input():
    n = int(input("Podaj liczbę równań: "))


    A = []
    b = []

    print("Wpisz kolejne współczynniki i wyniki ich po spacji")
    for i in range(n):
        line = input(f"Równanie x{i + 1}: ").strip().split()
        row = list(map(float, line))
        if len(row) != n + 1:
            print("Oczekiwano innej ilości liczb")
        A.append(row[:-1])
        b.append(row[-1])

    return A, b
