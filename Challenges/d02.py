#!/usr/bin/python

class D02:
    def __init__(self):
        pass
        
    def solve(self, commands):
        position = 0
        depth = 0
        for i in range(len(commands)):
            cmd_detail = commands[i].split(' ')
            amount = int(cmd_detail[1])
            if (cmd_detail[0] == 'forward'):
                position += amount
            elif (cmd_detail[0] == 'up'):
                depth -= amount
            elif (cmd_detail[0] == 'down'):
                depth += amount

        print('P1 - Position(' + str(position) + ') + Depth(' + str(depth) + ') = Answer(' + str(position * depth) +')')

        position = 0
        depth = 0
        aim = 0
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

        print('P2 - Position(' + str(position) + ') + Depth(' + str(depth) + ') = Answer(' + str(position * depth) +')')


if __name__ == '__main__':
    with open('../Files/02.input.txt') as file:
        commands = [line.strip() for line in file]
            
    solver = D02()
    solver.solve(commands)