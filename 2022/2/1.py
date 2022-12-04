scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

total_score = 0
for line in lines:
    [opponent, player] = line.split(' ')
    total_score += scores[player]

    if (scores[opponent] == scores[player]):
        total_score += 3

    if ((opponent == 'A' and player == 'Y') or (opponent == 'B' and player == 'Z') or (opponent == 'C' and player == 'X')):
        total_score += 6

print(total_score)
