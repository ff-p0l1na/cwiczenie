stan_konta = 0
polecenie = input(print("""Wybierz opcję:
saldo - Pobiera lub dodaje kwotę do konta.
sprzedaż - Pobiera nazwę produktu, cenę oraz liczbę sztuk.
zakup - Pobiera nazwę produktu, cenę oraz liczbę sztuk.
konto - Wyświetla stan konta.
lista - Wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn - Wyświetla stan magazynu dla konkretnego produktu.
przegląd - Wyświetla wszystkie wprowadzone akcje.
koniec - Aplikacja kończy działanie."""))

if polecenie == "saldo":
    decyzja_dla_salda = int(input("Jeśli chcesz pobrać pieniądze z konta naciśnij 1. Jeśli chcesz dodać naciśnij 2. "))
    if decyzja_dla_salda == 1:
        kwota_do_pobrania = float(input("Wpisz kwotę do pobrania z konta. "))
        stan_konta -= kwota_do_pobrania
    if decyzja_dla_salda ==2:
        kwota_do_dodania = float(input("Wpisz kwotę do dodania. "))
        stan_konta += kwota_do_dodania
if polecenie == "sprzedaż":
    nazwa_produktu = input("Podaj nazwę produktu. ")
    cena = float(input("Podaj cenę produktu. "))
    liczba_sztuk = int(input("Podaj ilość. "))
if polecenie == "zakup":
    nazwa_produktu = input("Podaj nazwę produktu. ")
    cena = float(input("Podaj cenę produktu. "))
    liczba_sztuk = int(input("Podaj ilość. "))
if polecenie == "konto":
    print(f"Stan konta wynosi {stan_konta} PLN")
if polecenie == "lista":
    print("tbd")
    #TODO napisac petle
if polecenie == "magazyn":
    print("tbd")
    #TODO napisac petle
if polecenie == "przegląd":
    print("tbd")
    #TODO napisac petle
if polecenie == "koniec":
    print("Koniec pracy programu.")