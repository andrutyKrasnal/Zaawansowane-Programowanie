def polaczListy(lista1: list[int], lista2: list[int]) -> list[int]:
    unikalne_liczby = set(lista1 + lista2)

    return[liczba **3 for liczba in unikalne_liczby]

listaA = [2, 1, 3, 7]
listaB = [6, 7, 6, 9]

print(polaczListy(listaA, listaB))