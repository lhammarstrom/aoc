with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

most = 0
sum = 0

for line in lines:
    if (line == ''):
        if (sum > most):
            most = sum
        sum = 0
    else:
        sum = sum + int(line)

print(most)
