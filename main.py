# 1.Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
# for sk in range(10):
#     print("labas")
from itertools import count

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



