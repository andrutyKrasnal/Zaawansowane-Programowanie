def czyParzysta(liczba: int) -> bool:
    return liczba % 2 ==0

parzysta = czyParzysta(67)

if parzysta:
    print("Liczba jest parzysta")
else:
    print("Liczba nie jest parzysta")
