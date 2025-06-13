import numpy as np

def gauss(lista_rownan, wyniki):

    lista_rownan = np.array(lista_rownan)
    wyniki = np.array(wyniki)
    liczba_rownan = len(wyniki)

    macierz_rozsz = np.hstack((lista_rownan, wyniki.reshape(-1, 1)))
    
    for i in range(liczba_rownan):
        max_row = i + np.argmax(np.abs(macierz_rozsz[i:, i]))
        macierz_rozsz[[i, max_row]] = macierz_rozsz[[max_row, i]]

        if np.abs(macierz_rozsz[i, i]) < 0.00001:
            raise ValueError("Brak jednoznacznego rozwiazania")
            return None

        for j in range(i + 1, liczba_rownan):
            wspolczynnik = macierz_rozsz[j, i] / macierz_rozsz[i, i]
            eliminowana_czesc = wspolczynnik * macierz_rozsz[i, i:]
            macierz_rozsz[j, i:] = macierz_rozsz[j, i:] - eliminowana_czesc

    x = np.zeros(liczba_rownan)
    for i in range(liczba_rownan - 1, -1, -1):
        #ostatni wynik
        wynik = macierz_rozsz[i, -1]
        suma_znanych = np.dot(macierz_rozsz[i, i + 1:liczba_rownan], x[i + 1:])
        licznik = wynik - suma_znanych
        mianownik = macierz_rozsz[i, i]
        x[i] = licznik / mianownik

    return x
