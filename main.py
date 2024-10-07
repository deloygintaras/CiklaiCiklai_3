# 1.Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
# for sk in range(10):
#     print("labas")
import random
from itertools import count
from random import randint

# 2. Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
# for sk in range(0, 9):
#     print(sk)


# 3. Sukurkite masyvą iš dešimties augalų pavadinimų.
# augalai = [
# "Roze",
# "Palmes",
# "Abrikosai",
# "Acenos",
# "Adonis",
# "Afelandra",
# "Agarai",
# "Agrastas",
# "Aguonaiciai",
# "Agurotis"
# ]
# print(augalai)



# 4. Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
# augalai = [
# "Roze",
# "Palmes",
# "Abrikosai",
# "Acenos",
# "Adonis",
# "Afelandra",
# "Agarai",
# "Agrastas",
# "Aguonaiciai",
# "Agurotis"
# ]
# for augalas in augalai:
#     print(augalas)



# 5. Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
# augalai = [
# "Roze",
# "Palmes",
# "Abrikosai",
# "Acenos",
# "Adonis",
# "Afelandra",
# "Agarai",
# "Agrastas",
# "Aguonaiciai",
# "Agurotis"
# ]
# for augalas in reversed(augalai):
#     print(augalas)

#
# # 6. Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
# for sk in range(10, 50, 2):
#     print(sk)


# 7. Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
# for sk in range(10, 50, 2):
#     print(sk)
#     if sk % 10 == 0:
#         continue
#     print(sk)

#2 sprednimas, kadangi su 1 ismeta po 2 kartus.
# for sk in range(10, 50):
#     if sk % 2 == 0:
#         if sk % 10 == 0:
#             continue
#         print(sk)

# 8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
# porsk = 0
# for i in range(0, 20):
#     print(i)
#     if i % 2 == 0:
#         porsk += 1
# print(f"Poriniu skaitmenu skaicius: {porsk}")


# 9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
# augalai = [
# "Roze",
# "Palmes",
# "Abrikosai",
# "Acenos",
# "Adonis",
# "Afelandra",
# "Agarai",
# "Agrastas",
# "Aguonaiciai",
# "Agurotis"
# ]
# maz = 0
# for i in augalai:
#     if len(i) < 5:
#         maz += 1
# print(f"Maziau nei 5 simboliai: {maz}")
#
# daug = 0
# for i in augalai:
#     if len(i) > 7:
#         daug += 1
# print(f"Daugiau nei 7 simboliai : {daug}")



# 10. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
# augalai = [
# "Roze",
# "Palmes",
# "Abrikosai",
# "Acenos",
# "Adonis",
# "Afelandra",
# "Agarai",
# "Agrastas",
# "Aguonaiciai",
# "Agurotis"
# ]
#
# salyga = 0
# for i in augalai:
#     if len(i) > 5 and len(i) < 10:
#         salyga += 1
# print(f"Ilgesniu nei 5 bet trumpesniu nei 10: {salyga}")


# SUNKESNI UZDAVINIAI:

# 1. Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

# didesniuz_150 = 0
# sk = [random.randint(0, 300) for i in range(300)]
# for atsk in sk:
#     if atsk > 150:
#         didesniuz_150 += 1
# print(f"Skaiciu didesniu uz 150 yra: {didesniuz_150}")
# for atsk in sk:
#     if atsk > 275:
#         print(f"[{atsk}]")
#     else:
#         print(atsk, end= ' ')


# 2. Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.
# sk = [random.randint(1, 3000) for i in range (3000)]
# print(sk)
# for sk1 in sk:
#     if sk1 % 77 == 0:
#         print(sk1, end= ', ')

# 2 sprendimas

# Generuojame 3000 atsitiktinių skaičių nuo 1 iki 3000
# sk = [random.randint(1, 3000) for i in range(3000)]
#
# # Renkame skaičius, dalijančius 77
# dali = [str(sk1) for sk1 in sk if sk1 % 77 == 0]
#
# # Spausdiname skaičius, atskirtus kableliais, be paskutinio kablelio
# print(', '.join(dali))




# 3. Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# krast = 25
# for i in range(krast):
#     print('*' * krast)


# 4. Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.




# 5. Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# a) Iškritus herbui;
# b) Tris kartus iškritus herbui;
# c) Tris kartus iš eilės iškritus herbui;




# 6. Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: laimėtojo vardas”.
# Taškų kiekį generuokite funkcija random.randint(x,x). Žaidimą laimi tas, kas greičiau surenka 222 taškus.
# Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.




# 7. Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą (https://lt.wikipedia.org/wiki/Rombas), kurio aukštis 21 eilutė.




# 8. Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija.
# Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# a) “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# b) “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm,
# bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.




# 9. Sugeneruokite stringą, kurį sudarytų 50 atsitiktinių skaičių nuo 1 iki 200, atskirtų tarpais. Skaičiai turi būti unikalūs (t.y. nesikartoti).
# Sugeneruokite antrą stringą, pasinaudodami pirmu, palikdami jame tik pirminius skaičius (t.y tokius, kurie dalinasi be liekanos tik iš 1 ir patys savęs).
# Skaičius stringe sudėliokite didėjimo tvarka, nuo mažiausio iki didžiausio. (reikės split() funkcijos ir masyvų.)




