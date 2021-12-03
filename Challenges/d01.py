#!/usr/bin/python

def solve(inputfile):

    with open(inputfile) as file:
        depths = [int(line.strip()) for line in file]

    increaseCount = 0
    prevDepth = depths[0]
    for i in range(1, len(depths)):
        currDepth = depths[i] 
        if prevDepth < currDepth:
            increaseCount = increaseCount + 1   
        prevDepth = currDepth      

    print('P1 - Linear IncreaseCount = ' + str(increaseCount))
            
    # Part 2 
    windowSize = 3
    increaseCount = 0
    prevDepthSum = sum(depths[:windowSize])
    for i in range(len(depths) - windowSize):
        currDepthSum = prevDepthSum - depths[i] + depths[i+windowSize]
        if (prevDepthSum < currDepthSum):
            increaseCount = increaseCount + 1
        
    print('P2 - Windowed IncreaseCount = ' + str(increaseCount))
        
if __name__ == '__main__':
    solve('../Files/01.input.txt')
        