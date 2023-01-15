f = open("Filepaths.txt", "r+")
lines = f.readlines()
for index, line in enumerate(lines):
    print(index)
    if index == 0:
        ctf = line.strip().split("=")
        print(ctf)
    else:
        segvar = line.strip()