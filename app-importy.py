plik_do_zapisu = open("history.txt", "a")
pliku_magazynowy = open("warehouse.txt", "a")
funkcje_programu = ("\n"
                    "########################\n"
                    "### DOSTĘPNE FUNKCJE ###\n"
                    "########################\n"
                    "saldo - Pobiera lub dodaje kwotę do konta.\n"
                    "sprzedaż - Pobiera nazwę produktu, cenę oraz liczbę sztuk.\n"
                    "zakup - Pobiera nazwę produktu, cenę oraz liczbę sztuk.\n"
                    "konto - Wyświetla stan konta.\n"
                    "lista - Wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.\n"
                    "magazyn - Wyświetla stan magazynu dla konkretnego produktu.\n"
                    "przegląd - Wyświetla wszystkie wprowadzone akcje.\n"
                    "koniec - Program kończy działanie.\n"
                    "######################\n")
mozliwe_akcje = ("saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przegląd", "koniec")
akcje = []
stan_konta: float = 0
magazyn = {}
# Magazyn = {
#     "produkt_1" : [ilosc_i_cena] }
ilosc_i_cena = []
while True:
    print(funkcje_programu)
    polecenie = input("Wpisz wybrane polecenie: ")
    if polecenie not in mozliwe_akcje:
        akcje.append(polecenie)
        plik_do_zapisu.write(f"\nPolecenie: {polecenie}. \n")
        print(f"Polecenie {polecenie} jest nieprawidłowe. \n"
              f"Wpisz polecenie ponownie: ")
    elif polecenie == "saldo":
        akcje.append(polecenie)
        plik_do_zapisu.write(f"\nPolecenie: {polecenie}. \n")
        decyzja_dla_salda = input('Jeśli chcesz POBRAĆ środki z konta, napisz "pobierz". \n'
                                  'Jeśli chcesz DODAĆ środki do konta, napisz "dodaj".')
        if decyzja_dla_salda == "pobierz":
            kwota_do_pobrania = float(input("Wpisz kwotę do pobrania z konta: "))
            akcje.extend([decyzja_dla_salda, kwota_do_pobrania])
            plik_do_zapisu.write(f"Decyzja: {decyzja_dla_salda}, kwota: {kwota_do_pobrania}.\n")
            weryfikuj_stan_konta = stan_konta - kwota_do_pobrania
            if weryfikuj_stan_konta <= 0:
                print(f"Uwaga! Stan konta po tej operacji nie może być mniejszy lub równy 0 PLN. \n"
                      f"Wpisz kwotę mniejszą niż {stan_konta} PLN. ")
            elif weryfikuj_stan_konta < 0:
                stan_konta -= kwota_do_pobrania
                print(f"Pobrano {kwota_do_pobrania} PLN. \n"
                      f"Na koncie pozostało {stan_konta} PLN. ")
        elif decyzja_dla_salda == "dodaj":
            kwota_do_dodania = float(input("Wpisz kwotę do dodania: "))
            plik_do_zapisu.write(f"Decyzja: {decyzja_dla_salda}, kwota: {kwota_do_dodania}.\n")
            if kwota_do_dodania < 0:
                print("Uspokój się, dodawana kwota musi być większa od 0. Spróbuj ponownie.")
                continue
            elif kwota_do_dodania >= 0:
                stan_konta += kwota_do_dodania
                akcje.extend([decyzja_dla_salda, kwota_do_dodania])
                print(f"Dodano {kwota_do_dodania} PLN.\n"
                  f"Aktualny stan konta to {stan_konta} PLN. ")
    elif polecenie == "sprzedaż":
        nazwa_produktu = input("Podaj nazwę produktu: ")
        akcje.extend([polecenie, nazwa_produktu])
        plik_do_zapisu.write(f"\nPolecenie: {polecenie}. Produkt: {nazwa_produktu}.\n")
        if nazwa_produktu not in magazyn:
            print(f"Uwaga, brak produktu: {nazwa_produktu} w magazynie.\n"
                  f"Spróbuj ponownie.")
            continue
        liczba_sztuk = int(input("Podaj ilość: "))
        cena = float(input("Podaj cenę jednostkową produktu: "))
        akcje.extend([liczba_sztuk, cena])
        plik_do_zapisu.write(f"Ilość: {liczba_sztuk}. Cena: {cena}.\n")
        if nazwa_produktu in magazyn:
            sprawdzana_ilosc_i_cena = magazyn.get(nazwa_produktu)
            sprawdzenie_dostepnosci = sprawdzana_ilosc_i_cena[0] - liczba_sztuk
            if sprawdzenie_dostepnosci <= 0:
                print(f"Uwaga! Za niski stan magazynowy dla produktu {nazwa_produktu}."
                      f"Pozostało sztuk: {sprawdzana_ilosc_i_cena[0]}. \n"
                      f"Spróbuj ponownie.")
                continue
            elif sprawdzenie_dostepnosci > 0:
                stan_konta += int(liczba_sztuk) * float(cena)
                ilosc_i_cena[0] -= liczba_sztuk
                pliku_magazynowy.writelines(f"stan magazynowy: {magazyn}")
    elif polecenie == "zakup":
        nazwa_produktu = input(">>> Podaj nazwę produktu:  ")
        liczba_sztuk = int(input(">>> Podaj ilość: "))
        cena = float(input(">>> Podaj cenę jednostkową produktu: "))
        akcje.extend([polecenie, nazwa_produktu, liczba_sztuk, cena])
        plik_do_zapisu.write(f"\nPolecenie: {polecenie}. Produkt: {nazwa_produktu}.\n "
                             f"Ilość: {liczba_sztuk}. Cena: {cena}.\n")
        sprawdz_stan_konta = stan_konta - int(liczba_sztuk) * float(cena)
        if sprawdz_stan_konta < 0:
            print("Uwaga! Nieprawidłowy stan konta po zakończeniu tej operacji. \n"
                  "Operacja niedozwolona. Przerywam akcję. ")
            continue
        elif sprawdz_stan_konta > 0:
            pass
        if nazwa_produktu not in magazyn:
            ilosc_i_cena = [0, 0]
            magazyn[str(nazwa_produktu)] = ilosc_i_cena
            ilosc_i_cena[0] = liczba_sztuk
            ilosc_i_cena[1] = cena
            stan_konta -= int(liczba_sztuk) * float(cena)
            pliku_magazynowy.writelines(f"magazyn: {magazyn}")
            print(f"Aktualizacja stanu magazynu. Dodano nowy produkt: \n"
                  f"produkt: {nazwa_produktu}\n"
                  f"ilość: {liczba_sztuk}\n"
                  f"cena jednostkowa: {cena} PLN\n")
        elif nazwa_produktu in magazyn:
            ilosc_i_cena = magazyn[str(nazwa_produktu)] # wywoluje ilosc i cene dla konkretnego produktu
            ilosc_i_cena[0] += int(liczba_sztuk) # dodaje do aktualnej liczby sztuk żądaną liczbę
            ilosc_i_cena[1] = float(cena) #podmieniam cene dla wszystkich sztuk na magazynie, kreatywna ksiegowosc.
            magazyn[str(nazwa_produktu)] = ilosc_i_cena # odswiezam półkę, na której dla wybranego produktu jest nowa l. sztuk i cena
            stan_konta -= int(liczba_sztuk) * float(cena)
            pliku_magazynowy.writelines(f"magazyn: {magazyn}\n")
            print(f"Aktualizacja stanu magazynu. \n"
                  f"Dodano {liczba_sztuk} do istniejącego produktu: {nazwa_produktu} \n"
                  f"Aktualna liczba sztuk i cena jednostkowa: {ilosc_i_cena}")
    elif polecenie == "konto":
        print(f"Aktualny stan konta wynosi {stan_konta} PLN.")
    elif polecenie == "lista":
        print(f"Stan magazynu (produkt: ilość, cena) to: \n"
              f"        {magazyn} ")
    elif polecenie == "magazyn":
        wybrany_produkt = input("Podaj nazwę produktu, \n"
                                "dla którego chcesz poznać stan magazynowy.")
        if wybrany_produkt not in magazyn:
            print(f"Błąd. Produkt {wybrany_produkt} nie istnieje.")
        elif wybrany_produkt in magazyn:
            stan_umyslu = magazyn[wybrany_produkt]
            print(f"Stan magazynowy dla {wybrany_produkt} to: (ilość, cena w PLN): \n"
                  f"{stan_umyslu} ")
    elif polecenie == "przegląd":
        wszystkie_akcje = input(f" Wykonano następującą liczbę operacji: {len(akcje)} .\n"
                                f"Wyświetlić wszystkie akcje? T/N : >>> ")
        if wszystkie_akcje == "T":
            print(akcje)
        else:
            print("Aby wyświetlić akcje w wybranym zakresie odpowiedz na 2 pytania: ")
            od = int(input(">>> OD której operacji rozpocząć? \n"
                           "Wpisz wybrany numer operacji: >>> "))
            do = int(input("Do której operacji wyświetlić akcje?\n"
                           "Wpisz numer ostatniej żądanej operacji: >>> "))
            print(f"Wybrano zakres od operacji nr {od} do operacji nr {do}.")
            od -= 1
            print(f"""W danym zakresie wykonano następujące akcje:
{akcje[od:do]}""")
    if polecenie == "koniec":
        print("Kończę pracę programu.")
        plik_do_zapisu.close()
        pliku_magazynowy.close()
        break
