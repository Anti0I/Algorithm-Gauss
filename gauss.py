import numpy as np

def gauss_elimination(lista_rownan, wyniki):

    lista_rownan = np.array(lista_rownan, dtype=float)
    wyniki = np.array(wyniki, dtype=float)
    liczba_rownan = len(wyniki)

    macierz_rozsz = np.hstack((lista_rownan, wyniki.reshape(-1, 1)))
    
    for i in range(liczba_rownan):
        max_row = i + np.argmax(np.abs(macierz_rozsz[i:, i]))
        macierz_rozsz[[i, max_row]] = macierz_rozsz[[max_row, i]]

        if np.abs(macierz_rozsz[i, i]) < 0.0000001:
            print("Brak jednoznacznego rozwiązania")
            return None

        for j in range(i + 1, liczba_rownan):
            factor = macierz_rozsz[j, i] / macierz_rozsz[i, i]
            eliminowana_czesc = factor * macierz_rozsz[i, i:]
            macierz_rozsz[j, i:] = macierz_rozsz[j, i:] - eliminowana_czesc

    x = np.zeros(liczba_rownan)
    #ogolnie to to moze nie byc zrozumialem ale daje sie od liczby rownan -1 bo
    # indeksy a potem z do -1 zeby raze wlacznie z 0 elementem to zrobic i -1 zeby od konca to robic ;)
    for i in range(liczba_rownan - 1, -1, -1):
        #ostatni wynik od konca
        wynik = macierz_rozsz[i, -1]
        #ta linijka sam nie zrobilem 
        suma_znanych = np.dot(macierz_rozsz[i, i + 1:liczba_rownan], x[i + 1:])
        licznik = wynik - suma_znanych
        mianownik = macierz_rozsz[i, i]
        x[i] = licznik / mianownik

    return x
#komentarz ode mnie algorytm sam w sobie prosty do zrobienia na kartce ale w pytohnie to to dosyc
#straszne duzo tych macierzy i po prostu wchodzenia gleboko do nich leb czasami zarywa 