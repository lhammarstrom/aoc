#         [Q] [B]         [H]
#     [F] [W] [D] [Q]     [S]
#     [D] [C] [N] [S] [G] [F]
#     [R] [D] [L] [C] [N] [Q]     [R]
# [V] [W] [L] [M] [P] [S] [M]     [M]
# [J] [B] [F] [P] [B] [B] [P] [F] [F]
# [B] [V] [G] [J] [N] [D] [B] [L] [V]
# [D] [P] [R] [W] [H] [R] [Z] [W] [S]
#  1   2   3   4   5   6   7   8   9

stacks = [
    ['V', 'J', 'B', 'D'],
    ['F', 'D', 'R', 'W', 'B', 'V', 'P'],
    ['Q', 'W', 'C', 'D', 'L', 'F', 'G', 'R'],
    ['B', 'D', 'N', 'L', 'M', 'P', 'J', 'W'],
    ['Q', 'S', 'C', 'P', 'B', 'N', 'H'],
    ['G', 'N', 'S', 'B', 'D', 'R'],
    ['H', 'S', 'F', 'Q', 'M', 'P', 'B', 'Z'],
    ['F', 'L', 'W'],
    ['R', 'M', 'F', 'V', 'S'],
]

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    # Example: move 7 from 7 to 2
    instructions = line.split(' ')
    amount = int(instructions[1])
    stack = int(instructions[3])-1
    destination = int(instructions[5])-1

    items_to_move = (stacks[stack][0:amount])
    items_to_move.reverse()

    for item in items_to_move:
        stacks[destination].insert(0, item)
        stacks[stack].remove(item)

message = ''
for stack in stacks:
    message += stack[0]

print(message)
