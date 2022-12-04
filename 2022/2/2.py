scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

plays = [
    'A',
    'B',
    'C',
]

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

total_score = 0
for line in lines:
    [opponent, outcome] = line.split(' ')

    player = opponent
    length = len(plays) - 1
    index = plays.index(opponent)

    play = index
    if (outcome == 'X'):
        play = index-1

    if (outcome == 'Z'):
        play = index+1

    if (play == -1):
        play = length
    elif (play == length+1):
        play = 0

    player = plays[play]
    total_score += scores[player]

    if (scores[opponent] == scores[player]):
        total_score += 3

    if ((opponent == 'A' and player == 'B') or (opponent == 'B' and player == 'C') or (opponent == 'C' and player == 'A')):
        total_score += 6

print(total_score)
