import numpy as np
A = np.array([[1, 2],
              [3, 4]])
b = np.array([[5],
              [98]])

Ab = np.hstack((A, b))
print(Ab)   

lista_rownan = [
    [2, 3, 4],
    [1, 4, 5],
    [4, 6, 5]
]
wyniki = [5, 6, 2]
lista_rownan = np.array(lista_rownan, dtype=float)
wyniki = np.array(wyniki, dtype=float)
print("wyniki jak tablica np ->",wyniki)
print("to jest reshape ->",wyniki.reshape(-1,1))
macierz_rozsz = np.hstack((lista_rownan, wyniki.reshape(-1, 1)))
print(macierz_rozsz)