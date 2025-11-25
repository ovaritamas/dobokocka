"""
Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5-ös dobás a listában?
2. Hanyadik dobás lett először 1-es?
3. Hány darab páros számot dobtunk?
4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?
5. Mennyi a 3-as dobások összege?
"""

import random
dobasok_szama = 20
dobasok = [random.randint(1, 6) for i in range (dobasok_szama)]
print(f"A dobások számai: {dobasok}")

#Volt 5-ös?

print("1. Volt-e 5-ös dobás a listában?")
van_otos = 5 in dobasok
print(f"Válasz: {'Igen' if van_otos else 'Nem'}")

#Első egyes

print("2. Hanyadik dobás lett először 1-es?")
elso_egyes_sorszam = -1
sorszam = 0

for dobas in dobasok:
    sorszam += 1
    if dobas == 1:
        elso_egyes_sorszam = sorszam
        break

if elso_egyes_sorszam != -1:
    print(f"Válasz: Az első 1-es dobás a {elso_egyes_sorszam}. helyen volt.")
else:
    print("Válasz: Nem volt 1-es dobás a listában.")

#Hány darab páros van?

print("3. Hány darab páros számot dobtunk?")
paros_darab = 0
for dobas in dobasok:
    if dobas % 2 == 0:
        paros_darab += 1
print(f"Válasz: {paros_darab} darab páros számot dobtunk.")

print("4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?")

legkisebb_negy_felett_sorszam = -1
legkisebb_negy_felett_ertek = 7
sorszam_4 = 0

for dobas_ertek in dobasok:
    sorszam_4 += 1
    
    if dobas_ertek > 4:
        if dobas_ertek < legkisebb_negy_felett_ertek:
            legkisebb_negy_felett_ertek = dobas_ertek
            legkisebb_negy_felett_sorszam = sorszam_4
        if legkisebb_negy_felett_ertek == 5:
            break

if legkisebb_negy_felett_sorszam != -1:
    print(f"Válasz: A legkisebb dobás a 4-nél nagyobbak közül a {legkisebb_negy_felett_ertek} volt. Először a {legkisebb_negy_felett_sorszam}. dobás volt.")
else:
    print("Válasz: Nem volt 4-nél nagyobb dobás a listában (5-ös vagy 6-os).")

#Hármasok összege

print("5. Mennyi a 3-as dobások összege?")
harmasok_szama = 0
for dobas in dobasok:
    if dobas == 3:
        harmasok_szama += 1
        
harmasok_osszege = harmasok_szama * 3
print(f"Válasz: {harmasok_szama} darab 3-as dobás volt, az összegük: {harmasok_osszege}")