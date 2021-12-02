#!/usr/bin/python

inputfile = 'puzzleInput.txt'

position = 0
depth = 0
aim = 0

with open(inputfile) as file:
    commands = [line.strip() for line in file]

for i in range(len(commands)):
    cmd_detail = commands[i].split(' ')
    amount = int(cmd_detail[1])
    if (cmd_detail[0] == 'forward'):
        position += amount
        depth += aim * amount
    elif (cmd_detail[0] == 'up'):
        aim -= amount
    elif (cmd_detail[0] == 'down'):
        aim += amount

print('Position:' + str(position) + ' Depth: ' + str(depth))
print('Answer: ' + str(position * depth))