
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

elves = []

sum = 0
for line in lines:
    if (line == ''):
        elves.append(sum)
        sum = 0
    else:
        sum = sum + int(line)

elves.sort(reverse=True)
top3 = elves[0]+elves[1]+elves[2]

print(top3)
