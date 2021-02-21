# Liste nedir?

# Nasıl oluşturulur?

liste_adi = []
liste_adi = ["zeki", "mustafa", "muhammed", "kerem", "ismet"]
# print(type(liste_adi))
# print(liste_adi)
# print(len(liste_adi))

# print(liste_adi[0])
# liste_adi.append("ordu")
# print(liste_adi[2:3])
# for i in liste_adi:
#     print(i)
liste_adi.insert(102, "aminoasit")
print(liste_adi)

for i in liste_adi:
    print(i.__str__())
