letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

chunks = []
chunk_size = 3

for i in range(0, len(lines), chunk_size):
    chunks.append(lines[i:i+chunk_size])

sum = 0
for chunk in chunks:
    first = set(chunk[0])
    second = set(chunk[1])
    third = set(chunk[2])

    common = first & second & third
    sum += letters.index(list(common)[0])+1

print(sum)
