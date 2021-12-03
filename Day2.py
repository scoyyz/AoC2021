x = 0
y = 0
course = []

with open("Day2.txt") as file:
    course = file.readlines()
    file.close()
    
    ##Part1##
# for move in course:
    # move = move.split()
    # if move[0] == "forward":
        # x += int(move[1])
    # elif move[0] == "up":
        # y -= int(move[1])
    # else:
        # y += int(move[1])
   
# print(x*y)

    ##Part 2##

aim = 0

for move in course:
    move = move.split()
    
    if move[0] == 'forward':
        x += int(move[1])
        y += int(move[1])*aim
    elif move[0] == 'up':
        aim -= int(move[1])
    else:
        aim += int(move[1])

print(x)
print(y)
print(x*y)