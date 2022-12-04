with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

contained = 0
for line in lines:
    sections = line.split(',')

    first = sections[0].split('-')
    second = sections[1].split('-')

    first_range = set(list(range(int(first[0]), int(first[1])+1)))
    second_range = set(list(range(int(second[0]), int(second[1])+1)))

    common = first_range & second_range
    if (len(common) > 0):
        contained += 1

print(contained)
