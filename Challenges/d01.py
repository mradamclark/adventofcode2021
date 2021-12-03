#!/usr/bin/python

class D01:
    def __init__(self):
        pass
    
    def solve(self, filedata):
        increaseCount = 0
        prevDepth = filedata[0]
        for i in range(1, len(filedata)):
            currDepth = filedata[i] 
            if prevDepth < currDepth:
                increaseCount = increaseCount + 1   
            prevDepth = currDepth      

        print('P1 - Linear IncreaseCount = ' + str(increaseCount))
                
        # Part 2 
        windowSize = 3
        increaseCount = 0
        prevDepthSum = sum(filedata[:windowSize])
        for i in range(len(filedata) - windowSize):
            currDepthSum = prevDepthSum - filedata[i] + filedata[i+windowSize]
            if (prevDepthSum < currDepthSum):
                increaseCount = increaseCount + 1
            
        print('P2 - Windowed IncreaseCount = ' + str(increaseCount))
        
if __name__ == '__main__':
    
    with open('../Files/01.input.txt') as file:
            depths = [int(line.strip()) for line in file]
    
    solver = D01()     
    solver.solve(depths)
        