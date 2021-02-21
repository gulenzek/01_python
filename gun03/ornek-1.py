numbers = input("Please give numbers(like 2,3,4,5,5.3): ").strip().split(",")
def isNumeric(val):
    if val.isdigit():
        return True
    elif val[0] == "-" and val[1:].isdigit():
        return True
    tmp = val + ""
    if tmp[0] == "-":
        tmp = tmp[1:]
    if tmp.replace(".","", 1).isdigit():
        return True
    return False
total = 0
for number in numbers:
    number = number.strip()
    if isNumeric(number):
        number = float(number)
        total += number
    else:
        total = None
        print("Invalid value")
        break
if total:
    print(total)
