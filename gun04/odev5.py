# Q5
# verilen "float" bir sayının, noktadan sonra kaç basamağı olduğunu hesaplayan bir program yazınız.

float_sayi = 87.2309349

sayi_list = str(float_sayi).split(".")

print(len(sayi_list[1]))