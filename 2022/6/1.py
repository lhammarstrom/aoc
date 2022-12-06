with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

markers = []
for line in lines:
    characters = list(line)

    for i in range(0, len(characters)):
        if (i >= 3):
            subset =\
                characters[i-3] + \
                characters[i-2] + \
                characters[i-1] + \
                characters[i]

            if (len(set(subset)) == len(subset)):
                markers.append(i+1)
                break

print(markers)
