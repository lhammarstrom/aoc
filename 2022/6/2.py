with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

markers = []
subset_length = 14

for line in lines:
    characters = list(line)

    for i in range(0, len(characters)):
        if (i >= subset_length):
            subset = ''.join(characters[i-subset_length:i])
            if (len(set(subset)) == len(subset)):
                markers.append(i)
                break

print(markers)
