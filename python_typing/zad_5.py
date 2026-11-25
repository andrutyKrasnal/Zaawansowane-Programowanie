def czyZawiera(lista: list[int], szukana: int) ->bool:
    return szukana in lista

liczby = [6, 7, 9, 2, 1, 3, 7, 67, 2137]
print(czyZawiera(liczby, 67))