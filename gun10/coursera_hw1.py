fname = input("Enter file name: ")
try:
    fh = open("words.txt")
except:
    print('Cannot open the file ', fname, 'please try again')
    quit()

for line in fh:
    line = line.upper()
    line = line.rstrip()
    print(line)
