#
# raw_data = """
# # 34AB123,123456,2009-12-11,Cayirova,asiri_hiz,100
# # 34AB123,999999,2009-12-11,SifaMah,asiri_hiz,200
# # 34AB999, 123456,2009-12-11,Cayirova,hatali_park,300
# # """.strip()
#
# satirlar = raw_data.splitlines()
#
# for satir in satirlar:
#     parcalar = satir.split(",")
#     print(parcalar)
#
#
# print("bitti")

raw_data = """
34AB123,123456,2009-12-11,Cayirova,asiri_hiz,100
34AB123 ,999999,2009-12-11,SifaMah,asiri_hiz,200
34AB999, 123456,2009-12-11,Cayirova,hatali_park,300
""".strip()
# her plakanin toplam cezasini hesaplayin.

satirlar = raw_data.splitlines()
cezalar = {}
for satir in satirlar:
    parcalar = satir.split(",")
    plaka = parcalar[0].strip()
    ceza_miktari = int(parcalar[5].strip())
    # print(parcalar)
    cezalar[plaka] = cezalar.get(plaka, 0) + ceza_miktari # önemli bir satır.. DİKKAT!!!

print(cezalar) # Döngünün içinden çıkardı..
print("bitti")