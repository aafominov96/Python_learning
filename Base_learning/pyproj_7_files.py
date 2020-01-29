def create_file(filename):
    with open(filename, 'w') as Baran:
        i = 0
        while i < 100:
            i += 1
            Baran.write('Hi, it\'s me! #')
            Baran.write(str(i))
            Baran.write("\n")
    pass

def read_file(filename):
    f = open(filename, 'r')
    return f

name = "text_file.txt"
create_file(name)
wf = read_file(name)
for stroka in wf:
    print(stroka)
    for bukva in stroka:
        print(bukva)
        if bukva == "#":
            print("I FIND THIS")
