#!/usr/bin/python3

import itertools;

if __name__ == '__main__':
    string_input = input();
    #print( itertools.groupby(string_input));
    
    for k,g in itertools.groupby(string_input):
        print("(%d, %s)" %(len(list(g)), k), end = ' ');
    
