#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    A = [ ];
    for _ in range(int(input())):
        A.append( input().split() );

    print(round(numpy.linalg.det(numpy.array(A, float)), 2));
    

