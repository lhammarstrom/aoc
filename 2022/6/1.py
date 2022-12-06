with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

markers = []
subset_length = 4

for line in lines:
    characters = list(line)

    for i in range(0, len(characters)):
        if (i >= 3):
            subset = ''
            for j in range(0, subset_length):
                subset += characters[i-j]

            if (len(set(subset)) == len(subset)):
                markers.append(i+1)
                break

print(markers)
