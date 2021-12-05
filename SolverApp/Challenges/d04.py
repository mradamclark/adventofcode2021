#!/usr/bin/python

import copy

class cell:
    def __init__(self, value):
        self.value = value
        self.called = False
    
    def set_called(self, called_value):
        if (self.value == called_value):
            self.called = True
    
    def is_called(self):
        return self.called
    
    def __str__(self):
        called_char = 'T' if self.called else 'F'
        return '{}/{}'.format(self.value, called_char)
        

class board:

    def __init__(self, data):
        self.__cells = []
        for i in range(0,len(data)):
            self.__cells.extend([cell(x) for x in data[i].split()])
        
    def call_number(self, n):
        for c in self.__cells:
            c.set_called(n)
    
    def is_winner(self):
        if (self.is_row_winner()):
            return True
        
        if (self.is_col_winner()):
            return True

        return False
   
    def is_row_winner(self):
        for i in range(0,len(self.__cells),5):
            iswinner = all( c.is_called() for c in self.__cells[i:i+5])
            if (iswinner):
                return True
        return False
    
    def is_col_winner(self):
        for i in range(0, 4):
            iswinner = all(c.is_called() for c in self.__cells[i::5])
            if (iswinner):
                return True
        return False
            
    def sum_uncalled_numbers(self):
        return sum([int(c.value) for c in self.__cells if not c.is_called()])
        
    def __str__(self):
        s = ''
        for i in range(0,len(self.__cells), 5):
            s += ' '.join([str(x) for x in self.__cells[i:i+5]]) + '\n'
        return s

class d04:
    def __init__(self):
        pass

    def solve_p1(self, boards, numbers):
        winner = None
        for n in numbers:
            lastn = n
            for b in boards:
                b.call_number(n)
                if (b.is_winner()):
                    winner = b
                    break
            if (winner != None):
                break
                    
        sum_of_uncalled_n = winner.sum_uncalled_numbers()
        print(str(winner))
        print('lastn: {}'.format(lastn))
        print('Sum Of Uncalled: {}'.format(sum_of_uncalled_n))
        print('Board Answer: {}'.format(sum_of_uncalled_n * int(lastn)))
        print('\n')
        
    def solve_p2(self, boards, numbers):
        
        winner = None
        for n in numbers:
            lastn = n
            losers = []
            for b in boards:
                b.call_number(n)
                if (b.is_winner()):
                    winner = b
                else:
                    losers.append(b)
            boards = losers
            if len(boards) == 0:
                break
                    
        sum_of_uncalled_n = winner.sum_uncalled_numbers()
        print(str(winner))  
        print('lastn: {}'.format(lastn))
        print('Sum Of Uncalled: {}'.format(sum_of_uncalled_n))
        print('Board Answer: {}'.format(winner.sum_uncalled_numbers() * int(lastn)))  
        print('\n')       

    def solve(self, data):
        boards = []
        for i in range(2, len(data), 6):
            b = board(data[i:i+5])
            boards.append(b)
        
        call_numbers = data[0].split(',')
        self.solve_p1(copy.deepcopy(boards), call_numbers)
        self.solve_p2(copy.deepcopy(boards), call_numbers)

if __name__ == '__main__':
    with open('../../Files/04.test.txt') as file:
            data = [line.strip() for line in file]
    solver = d04()
    solver.solve(data) 