# Q1 middlestrip()
# Bir string alıp, içindeki boşlukları silen bir fonksiyon yazınız.
# Bu işlem sonrasında, parametrenin solundaki ve sağındaki boşluklar kalıyor olmalıdır.
#
# "   aa b c   "
# "   aabc   "
#
# def middlestrip(string1):
#     pass
# @author: Zeki Gülen, 17/10/2020

def middlestrip(lakirti):
    return (len(lakirti) - len(lakirti.lstrip())) * " " + "".join(lakirti.split()) + (
                len(lakirti) - len(lakirti.rstrip())) * " "


terim = "            a b  "
terim1 = "  A \n  a d@  1  2 \t"
terim2 = "   aa b c   "

print(middlestrip(terim))
print(middlestrip(terim1))
print(middlestrip(terim2))

#print("".join(terim2.split())) # thanks to Roger Pate on https://stackoverflow.com/questions/3739909/how-to-strip-all-whitespace-from-string

