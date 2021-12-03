#!/usr/bin/python

def solve():
    inputfile = '../Files/01.input.txt'

    increaseCount = 0
    depths = []

    with open(inputfile) as file:
        depths = [int(line.strip()) for line in file]

        prevDepth = depths[0]
        for i in range(len(depths)):
            currDepth = depths[i]
                
            if prevDepth < currDepth:
                increaseCount = increaseCount + 1
                
            prevDepth = currDepth      

    print('Linear IncreaseCount = ' + str(increaseCount))
            
    # Part 2 
    depths = []
    k = 3;
    increaseCount = 0

    with open(inputfile) as file:
        depths = [int(line.strip()) for line in file]
        
    prevDepthSum = sum(depths[:k])
    for i in range(len(depths) - k):
        currDepthSum = prevDepthSum - depths[i] + depths[i+k]
        if (prevDepthSum < currDepthSum):
            increaseCount = increaseCount + 1
        
    print('Windowed IncreaseCount = ' + str(increaseCount))
        
if __name__ == '__main__':
    solve()
        