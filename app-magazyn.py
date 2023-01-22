# Setup
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
# magazyn = {
#     "produkt_1" : [ilosc, cena],
#     "produkt_2" : [ilosc, cena] }
menu = True
# Start
while True:
    print(funkcje_programu)
    polecenie = input(""">>> Wpisz wybrane polecenie: """)
    if polecenie not in mozliwe_akcje:
        menu = False
        print(f"""Polecenie {polecenie} jest nieprawdiłowe.
>>> Wpisz polecenie ponownie: """)
        menu += 1
    if polecenie == "saldo":
        menu = False
        akcje.append(polecenie)
        decyzja_dla_salda = input(""">>> Jeśli chcesz POBRAĆ środki z konta, napisz \"pobierz\". 
>>> Jeśli chcesz DODAĆ środki do konta, napisz \"dodaj\".""")
        if decyzja_dla_salda == "pobierz":
            kwota_do_pobrania = float(input(">>> Wpisz kwotę do pobrania z konta: "))
            stan_konta -= kwota_do_pobrania
            if stan_konta < 0:
                stan_konta += kwota_do_pobrania
                print(f"""Uwaga! Stan konta po tej operacji nie może być mniejszy niż 0 PLN. 
>>> Wpisz kwotę mniejszą niż {stan_konta} PLN: """)
                decyzja_dla_salda = "pobierz"
            else:
                akcje.append(decyzja_dla_salda)
                akcje.append(kwota_do_pobrania)
                print(f"""Pobrano {kwota_do_pobrania} PLN. 
Na koncie pozostało {stan_konta} PLN. """)
                menu = True
        if decyzja_dla_salda == "dodaj":
            akcje.append(decyzja_dla_salda)
            kwota_do_dodania = float(input(">>> Wpisz kwotę do dodania: "))
            stan_konta += kwota_do_dodania
            akcje.append(kwota_do_dodania)
            print(f"""Dodano {kwota_do_dodania} PLN.
Aktualny stan konta to {stan_konta} PLN. """)
            menu = True
    if polecenie == "sprzedaż":
        menu = False
        nazwa_produktu = input(">>> Podaj nazwę produktu: ")
        liczba_sztuk = int(input(">>> Podaj ilość: "))
        cena = float(input(">>> Podaj cenę produktu: "))
        # Produkt musi znajdować się w magazynie.
        if nazwa_produktu in magazyn:
            stan_konta =+ liczba_sztuk * cena
            menu += 1
    if polecenie == "zakup":
        menu = False
        nazwa_produktu = input(">>> Podaj nazwę produktu:  ")
        liczba_sztuk = int(input(">>> Podaj ilość: "))
        cena = float(input(">>> Podaj cenę jednostkową produktu: "))
        stan_konta -= liczba_sztuk * cena
        if stan_konta < 0:
            print("""Uwaga! Ujemna wartość konta po zakończeniu tej operacji.
Operacja niedozwolona.
Przerywam transakcję. """)
            stan_konta += liczba_sztuk * cena
            menu = True
        else:
            ilosc_i_cena.extend([liczba_sztuk, cena])
            magazyn[(str(nazwa_produktu))] = ilosc_i_cena
            akcje.extend([polecenie, nazwa_produktu, liczba_sztuk, cena])
            print(f"""Aktualizacja stanu magazynu:
produkt: {nazwa_produktu}
dodano sztuk: {liczba_sztuk}
cena jednostkowa: {cena} 
""")
            menu = True
    if polecenie == "konto":
        menu = False
        print(f"Aktualny stan konta wynosi {stan_konta} PLN.")
        menu += 1
    if polecenie == "lista":
        menu = False
        print(magazyn)
        menu += 1
    if polecenie == "magazyn":
        menu = False
        wybrany_produkt = input("""Podaj nazwę produktu, 
dla którego chcesz poznać stan magazynowy.""")
        #TODO reszta
        menu += 1
    if polecenie == "przegląd":
        menu = False
        wszystkie_akcje = input(f""" Wykonano następującą liczbę operacji: {len(akcje)} .
Wyświetlić wszystkie akcje? T/N : >>> """)
        if wszystkie_akcje == "T":
            print(akcje)
            menu = True
        else:
            print("""Aby wyświetlić akcje w wybranym zakresie odpowiedz na 2 pytania: """)
            od = int(input(""">>> OD której operacji rozpocząć? 
Wpisz wybrany numer operacji: >>> """))
            do = int(input("""Do której operacji wyświetlić akcje?
Wpisz numer ostatniej żądanej operacji: >>> """))
            print(f"Wybrano zakres od operacji nr {od} do operacji nr {do}.")
            od -= 1 # bo index zaczyna sie od 0; nie trzeba odejmowac 1 od zmiennej "do", bo index "stop" jest elusive (nie "wlącznie")
            print(f"""W danym zakresie wykonano następujące akcje:
{akcje[od:do]}""")
            menu += 1
    if polecenie == "koniec":
       print("Kończę pracę programu.")
       break



