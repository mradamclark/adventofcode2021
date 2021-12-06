#!/usr/bin/python

class d06:
    def __init__(self):
        pass

    def solve(self, data):
        fish = [0]*9
        for i in list(map(lambda x:int(x.strip()), data[0].split(','))):
            fish[i] += 1
        
        days = 80
        print('{}: {}'.format(' I', fish))
        for n in range(days):
            oldfish = 0
            newfish = 0
            if (fish[0] != 0):
                oldfish = int(fish[0])
                newfish = int(oldfish)
                fish[0] = 0
            
            for i in range(1,len(fish)):
                    fish[i-1] = fish[i]
            
            fish[6] += oldfish
            fish[8] = newfish
            print('{:02d}: {}'.format(n, fish))
        
        print(sum(fish))
          
        

if __name__ == '__main__':
    with open('../../Files/06.test.txt') as file:
            data = [line.strip() for line in file]
    solver = d06()
    solver.solve(data) 

    