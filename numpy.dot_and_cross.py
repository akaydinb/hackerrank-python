#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    N = int(input());
    #A = numpy.array( input().split(), int);
    #B = numpy.array( input().split(), int);
    A = [ ]; B = [ ];
    for _ in range(N):
        A.append( input().split() );

    for _ in range(N):
        B.append( input().split() );

    matA = numpy.array(A, int);
    matB = numpy.array(B, int);

    print( matA.dot(matB))
