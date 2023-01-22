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
koniec - Aplikacja kończy działanie.
######################
"""
mozliwe_akcje = ("saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przegląd", "koniec")
akcje = []
stany_magazynowe = {}
ceny_produktow = {}
stan_konta = 0
menu = True
while True:
    print(funkcje_programu)
    polecenie = input("""Wpisz wybrane polecenie: """)
    if polecenie not in mozliwe_akcje:
        menu = False
        print(f"""Polecenie {polecenie} jest nieprawdiłowe.
        
Wpisz polecenie ponownie: """)
        menu += 1
    if polecenie == "saldo":
        menu = False
        akcje.append(polecenie)
        decyzja_dla_salda = input("""Jeśli chcesz POBRAĆ środki z konta, napisz \"pobierz\". 

Jeśli chcesz DODAĆ środki do konta, napisz \"dodaj\".""")
        if decyzja_dla_salda == "pobierz":
            akcje.append(decyzja_dla_salda)
            kwota_do_pobrania = float(input("Wpisz kwotę do pobrania z konta: "))
            stan_konta -= kwota_do_pobrania
            if stan_konta < 0:
                stan_konta += kwota_do_pobrania
                print(f"""Uwaga! Stan konta po tej operacji nie może być mniejszy niż 0 PLN. 
Wpisz kwotę mniejszą niż {stan_konta} PLN:
""")
                decyzja_dla_salda = "pobierz"
            else:
                akcje.append(kwota_do_pobrania)
                print(f"""Pobrano {kwota_do_pobrania} PLN. 
Na koncie pozostało {stan_konta} PLN. 
""")
                menu = True
        if decyzja_dla_salda == "dodaj":
            akcje.append(decyzja_dla_salda)
            kwota_do_dodania = float(input("Wpisz kwotę do dodania: "))
            stan_konta += kwota_do_dodania
            akcje.append(kwota_do_dodania)
            print(f"""Dodano {kwota_do_dodania} PLN.
Aktualny stan konta to {stan_konta} PLN. """)
            menu = True
    if polecenie == "sprzedaż":
        menu = False
        nazwa_produktu = input("Podaj nazwę produktu. ")
        cena = float(input("Podaj cenę produktu. "))
        liczba_sztuk = int(input("Podaj ilość. "))
        print(f"""Dodano produktów: {liczba_sztuk} """)
        menu += 1
    if polecenie == "zakup":
        menu = False
        nazwa_produktu = input("Podaj nazwę produktu. ")
        cena = float(input("Podaj cenę produktu. "))
        liczba_sztuk = int(input("Podaj ilość. "))
        print(f"""Dodano {nazwa_produktu} w ilosci {liczba_sztuk} . 
Cena za sztuke to {cena}. """)
        menu += 1
    if polecenie == "konto":
        menu = False
        print(f"Aktualny stan konta wynosi {stan_konta} PLN.")
        menu += 1
    if polecenie == "lista":
        menu = False
        print("TBD")
        menu += 1
        #TODO napisac to
    if polecenie == "magazyn":
        menu = False
        print(stany_magazynowe)
        menu += 1
        #TODO napisac to
    if polecenie == "przegląd":
        menu = False
        print(f"""Wykonano następujące akcje: 
{akcje} """)
        menu += 1
    if polecenie == "koniec":
       print("Kończę pracę programu.")
       break



