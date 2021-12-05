#!/usr/bin/python

import sys, getopt
from Challenges import *


_target_days = []
_inputfile_name = ""

def usage():
    print ("Usage: ./solver.py -d <target-day> -i <inputfile> ")
    print ("\t-d <target-day> - can be 'all' or a list of exploits seperated by ','")
    print ("\t-i <inputfile> - optional,  data set to run against")  

def parse_args():
    global _target_days, _inputfile_name
    if len(sys.argv) < 3:
        usage()
        
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'd:i:') 
        for o in opts:
            if o[0] == "-d":
                _target_days = [int(s.strip()) for s in o[1].split(',')]
            elif o[0] == "-i":
                _inputfile_name = o[1]
            else:
                print("Option " + o[0] + " not recognized")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
        
def run_solver():
    with open(_inputfile_name) as file:
            data = [int(line.strip()) for line in file]
    
    klass = globals()['d01']
    print(klass)
    solver = klass()
    solver.solve(data)

if __name__ == '__main__':
    parse_args()
    run_solver()
