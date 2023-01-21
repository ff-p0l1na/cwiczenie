# zmienne
liczba_paczek_wyslanych = 0
liczba_kg_wyslanych = 0
waga_najlzejszej_paczki = 20
nr_najlzejszej_paczki = None
waga_aktualnej_paczki = 0
# petla
# wczytaj podana przez usera liczbe elementow do zmiennej liczba_elementow_do_wyslania
liczba_elementow_do_wyslania = int(input("Podaj liczbę elemenótw do wysłania: "))
# dla kazdego elementu z zakresu liczba_elementow_do_wyslania
# wczytaj wage elementu podana przez usera do zmiennej waga aktualnego elementu
for element in range(liczba_elementow_do_wyslania):
    waga_aktualnego_elementu = float(input("Podaj wagę elementu: "))
# jesli waga elementu nie jest w zakresie 1-10: przerwij wczytywanie elementow
    if waga_aktualnego_elementu > 10 or waga_aktualnego_elementu < 1:
        print("Nieprawidłowa waga elementu.")
        break
# jesli waga jest w zakresie 1-10, dodaj wage aktualnego elementu do wagi aktualnej paczki:
    waga_aktualnej_paczki += waga_aktualnego_elementu
# scenariusz jesli waga aktualnej paczki to wiecej niz 20 kg:
    if waga_aktualnej_paczki > 20:
        waga_aktualnej_paczki -= waga_aktualnego_elementu
        liczba_paczek_wyslanych += 1
        if waga_aktualnej_paczki < waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_aktualnej_paczki
            nr_najlzejszej_paczki = liczba_paczek_wyslanych
        liczba_kg_wyslanych += waga_aktualnej_paczki
        waga_aktualnej_paczki = waga_aktualnego_elementu
# scenariusz jak paczka wazy rowne 20 kg:
    if waga_aktualnej_paczki == 20:
        liczba_paczek_wyslanych += 1
        if waga_aktualnej_paczki < waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = waga_aktualnej_paczki
            nr_najlzejszej_paczki = liczba_paczek_wyslanych
        liczba_kg_wyslanych += waga_aktualnej_paczki
        waga_aktualnej_paczki = 0
# scenariusz jak paczka wazy mniej niz 20 kg:
    if waga_aktualnej_paczki < 20:
        pass
if waga_aktualnej_paczki > 0:
    liczba_paczek_wyslanych += 1
    liczba_kg_wyslanych += waga_aktualnej_paczki
# podsumowanie
print(f"Liczba paczek wysłanych to {liczba_paczek_wyslanych}.")
print(f"Wysłano łącznie {liczba_kg_wyslanych} kg.")
print(f"Najlżejsza paczka ma nr {nr_najlzejszej_paczki}.")
puste_kg = liczba_paczek_wyslanych * 20 - liczba_kg_wyslanych
print(f"Wysłano następującą ilość \"pustych\" kg: {puste_kg} .")