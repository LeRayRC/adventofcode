# Challenge 1

with open('input.txt') as f:
    lines = f.readlines()

movements=[x.strip() for x in lines]

horizontal = 0
depth = 0

for i in range(0,len(movements)):
    split_move = movements[i].split()
    dir = split_move[0]
    unit = int(split_move[1])

    if dir == "forward":
        horizontal += unit
    elif dir == "down":
        depth += unit
    else:
        depth -= unit

final_value = horizontal*depth

print(final_value)

# Challenge 2

horizontal = 0
depth = 0
aim = 0

for i in range(0,len(movements)):
    split_move = movements[i].split()
    dir = split_move[0]
    unit = int(split_move[1])

    if dir == "forward":
        horizontal += unit
        depth += unit*aim
    elif dir == "down":
        aim += unit
    else:
        aim -= unit

final_value = horizontal*depth

print(final_value)