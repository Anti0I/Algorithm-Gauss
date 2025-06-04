import numpy as np

def gauss_elimination(A, b):

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    Ab = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        max_row = i + np.argmax(np.abs(Ab[i:, i]))
        Ab[[i, max_row]] = Ab[[max_row, i]]

        if np.abs(Ab[i, i]) < 0.0000001:
            raise ValueError("Brak jednoznacznego rozwiązania")

        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:])) / Ab[i, i]

    return x
