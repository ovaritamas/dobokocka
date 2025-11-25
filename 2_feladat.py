"""
Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
A bevitel végét a 0.0 jelzi.
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5.5-nél nagyobb szám a listában?
2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!
3. Hány darab 1 és 2 közé eső szám szerepel a listában?
4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
5. Mennyi a pozitív számok összege?
"""
import math

def float_elemzes():

    szamok_lista = []
    while True:
        try:
            beolvasott_szam = float(input("Adj egy számot: "))
            
            if beolvasott_szam == 0.0:
                break
            szamok_lista.append(beolvasott_szam)
            
        except ValueError:
            print("Hibás bemenet! Kérem, tizedes törtet adjon meg.")
            continue
        print(f"A feldolgozandó számok listája: {szamok_lista}")
        if not szamok_lista:
            print("Nincs adat a listában. A feladatok megoldása kihagyva.")
        return
    
    print("1. Volt-e 5.5-nél nagyobb szám a listában?")
    van_5_pont_5_feletti = any(szam > 5.5 for szam in szamok_lista)
    print(f"Válasz: {'Igen' if van_5_pont_5_feletti else 'Nem'}")
    print("2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0)!")
    elso_negativ_egesz_index = -1
    for index, szam in enumerate(szamok_lista):
        if szam < 0 and szam == math.floor(szam):
            elso_negativ_egesz_index = index
            break
        if elso_negativ_egesz_index != -1:
            print(f"Válasz: Az első ilyen szám indexe (pozíciója) a listában: {elso_negativ_egesz_index}")
    else:
        print("Válasz: Nem találtunk negatív, egész számot a listában.")