branslar = ("Yazılım", "Tasarım", "Pazarlama")
tum_ogrenciler = []
ogrenci1 = ["Muhammed", ["Yazılım"]]
ogrenci2 = ["Ömer", ["Tasarım", "Pazarlama"]]
ogrenci3 = ["Esra", ["Pazarlama"]]
tum_ogrenciler.append(ogrenci1)
tum_ogrenciler.append(ogrenci2)
tum_ogrenciler.append(ogrenci3)

ogrenci1[0] = ogrenci1[0].strip()
ogrenci2[0] = ogrenci2[0].strip()
ogrenci3[0] = ogrenci3[0].strip()

print("Initial Student List:", tum_ogrenciler)

baskan = ["Ayfer", ["Yazılım"]]
tum_ogrenciler.insert(0, baskan)

print("Total Registered Students:", len(tum_ogrenciler))

tum_ogrenciler.remove(ogrenci2)

son_ogrenci = tum_ogrenciler.pop()

print("Sistemden en son çıkan öğrenci:", son_ogrenci[0])

figen = ["Figen", ["Tasarım"]]
tum_ogrenciler.append(figen)

gecici_liste = sorted(tum_ogrenciler)

print("Temporary Sorted List:", gecici_liste)
print("Original List:", tum_ogrenciler)

tum_ogrenciler.sort()

print("Permanently Sorted List:", tum_ogrenciler)
