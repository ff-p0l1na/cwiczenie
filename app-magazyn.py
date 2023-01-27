funkcje_programu = """
########################
### DOSTĘPNE FUNKCJE ###
########################
saldo - Pobiera lub dodaje kwotę do konta.
sprzedaż - Pobiera nazwę produktu, cenę oraz liczbę sztuk.
zakup - Pobiera nazwę produktu, cenę oraz liczbę sztuk.
konto - Wyświetla stan konta.
lista - Wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn - Wyświetla stan magazynu dla konkretnego produktu.
przegląd - Wyświetla wszystkie wprowadzone akcje.
koniec - Program kończy działanie.
######################
"""
mozliwe_akcje = ("saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przegląd", "koniec")
akcje = []
stan_konta = 0
magazyn = {}
ilosc_i_cena = []
# Magazyn = {
#     "produkt_1" : [ilosc, cena],
#     "produkt_2" : [ilosc, cena] }
while True:
    print(funkcje_programu)
    polecenie = input("Wpisz wybrane polecenie: ")
    if polecenie not in mozliwe_akcje:
        akcje.append(polecenie)
        print(f"""Polecenie {polecenie} jest nieprawdiłowe. 
Wpisz polecenie ponownie: """)
    elif polecenie == "saldo":
        akcje.append(polecenie)
        decyzja_dla_salda = input("""Jeśli chcesz POBRAĆ środki z konta, napisz \"pobierz\". 
Jeśli chcesz DODAĆ środki do konta, napisz \"dodaj\".""")
        if decyzja_dla_salda == "pobierz":
            akcje.append(decyzja_dla_salda)
            kwota_do_pobrania = float(input("Wpisz kwotę do pobrania z konta: "))
            akcje.append(kwota_do_pobrania)
            stan_konta -= kwota_do_pobrania
            if stan_konta < 0:
                stan_konta += kwota_do_pobrania
                print(f"""Uwaga! Stan konta po tej operacji nie może być mniejszy lub równy 0 PLN. 
Wpisz kwotę mniejszą niż {stan_konta} PLN: """)
            else:
                print(f"""Pobrano {kwota_do_pobrania} PLN. 
Na koncie pozostało {stan_konta} PLN. """)
        elif decyzja_dla_salda == "dodaj":
            kwota_do_dodania = float(input("Wpisz kwotę do dodania: "))
            stan_konta += kwota_do_dodania
            akcje.extend([decyzja_dla_salda, kwota_do_dodania])
            print(f"""Dodano {kwota_do_dodania} PLN.
Aktualny stan konta to {stan_konta} PLN. """)
    elif polecenie == "sprzedaż":
        nazwa_produktu = input(">>> Podaj nazwę produktu: ")
        akcje.extend([polecenie, nazwa_produktu])
        if nazwa_produktu not in magazyn:
            print(f"""Uwaga, brak produktu: {nazwa_produktu} w magazynie.
Wybierz ponownie.""")
        liczba_sztuk = int(input("Podaj ilość: "))
        cena = float(input("Podaj cenę jednostkową produktu: "))
        akcje.extend([liczba_sztuk, cena])
        if nazwa_produktu in magazyn:
            sprawdzenie_dostepnosci = ilosc_i_cena[0] - int(liczba_sztuk)
            if sprawdzenie_dostepnosci <= 0:
                print(f"""Uwaga! Za niski stan magazynowy dla produktu {nazwa_produktu}.
Spróbuj ponownie.""")
            elif sprawdzenie_dostepnosci > 0:
                stan_konta += int(liczba_sztuk) * float(cena)
        elif nazwa_produktu not in magazyn:
            print(f"""Nie znaleziono produktu {nazwa_produktu} .
Podany produkt nie znajduje się w magazynie.""")
    elif polecenie == "zakup":
        nazwa_produktu = input(">>> Podaj nazwę produktu:  ")
        liczba_sztuk = int(input(">>> Podaj ilość: "))
        cena = float(input(">>> Podaj cenę jednostkową produktu: "))
        akcje.extend([polecenie, nazwa_produktu, liczba_sztuk, cena])
        sprawdz_stan_konta = stan_konta - int(liczba_sztuk) * float(cena)
        if sprawdz_stan_konta < 0:
            print("""Uwaga! Nieprawidłowy stan konta po zakończeniu tej operacji. 
Operacja niedozwolona. Przerywam akcję. """)
        elif sprawdz_stan_konta > 0:
            stan_konta -= int(liczba_sztuk) * float(cena)
        if nazwa_produktu not in magazyn:
            ilosc_i_cena = [0, 0]
            ilosc_i_cena[0] = liczba_sztuk
            ilosc_i_cena[1] = cena
            magazyn[str(nazwa_produktu)] = ilosc_i_cena
            print(f"""Aktualizacja stanu magazynu. Dodano:
produkt: {nazwa_produktu}
dodano sztuk: {liczba_sztuk}
cena jednostkowa: {cena} PLN
""")
        elif nazwa_produktu in magazyn:
            ilosc_i_cena[0] += int(liczba_sztuk)
            ilosc_i_cena[1] = float(cena)
    elif polecenie == "konto":
        print(f"Aktualny stan konta wynosi {stan_konta} PLN.")
    elif polecenie == "lista":
        caly_magazyn = magazyn
        print(f"""Stan magazynu (produkt: ilość, cena) to:"
        {magazyn} """)
    elif polecenie == "magazyn":
        wybrany_produkt = input("""Podaj nazwę produktu, 
dla którego chcesz poznać stan magazynowy.""")
        if wybrany_produkt not in magazyn:
            print(f"Błąd. Produkt {wybrany_produkt} nie istnieje.")
        elif wybrany_produkt in magazyn:
            stan_umyslu = magazyn[wybrany_produkt]
            print(f"""Stan magazynowy dla {wybrany_produkt} to: (ilość, cena w PLN): 
{stan_umyslu} """)
    elif polecenie == "przegląd":
        wszystkie_akcje = input(f""" Wykonano następującą liczbę operacji: {len(akcje)} .
Wyświetlić wszystkie akcje? T/N : >>> """)
        if wszystkie_akcje == "T":
            print(akcje)
        else:
            print("""Aby wyświetlić akcje w wybranym zakresie odpowiedz na 2 pytania: """)
            od = int(input(""">>> OD której operacji rozpocząć? 
Wpisz wybrany numer operacji: >>> """))
            do = int(input("""Do której operacji wyświetlić akcje?
Wpisz numer ostatniej żądanej operacji: >>> """))
            print(f"Wybrano zakres od operacji nr {od} do operacji nr {do}.")
            od -= 1
            print(f"""W danym zakresie wykonano następujące akcje:
{akcje[od:do]}""")
    if polecenie == "koniec":
       print("Kończę pracę programu.")
       break



