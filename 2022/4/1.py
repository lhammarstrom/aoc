with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

contained = 0
for line in lines:
    sections = line.split(',')

    first = sections[0].split('-')
    second = sections[1].split('-')

    first_range = list(range(int(first[0]), int(first[1])+1))
    second_range = list(range(int(second[0]), int(second[1])+1))

    first_is_contained_in_second = all(
        elem in first_range for elem in second_range)
    second_is_contained_in_first = all(
        elem in second_range for elem in first_range)

    if (first_is_contained_in_second or second_is_contained_in_first):
        contained += 1

print(contained)
