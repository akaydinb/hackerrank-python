#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    [ N, M ] = input().split();
    L = [ ];
    for _ in range(int(N)):
        L.append(input().split());
    #print(L)
    A = numpy.array(L, int);

    L = [ ];
    for _ in range(int(N)):
        L.append(input().split());
    #print(L)
    B = numpy.array(L, int);

#    A = numpy.array( input().split(), int);
#    B = numpy.array( input().split(), int);

    print( numpy.add(A, B),      sep = '' );
    print( numpy.subtract(A, B), sep = '' );
    print( numpy.multiply(A, B), sep = '' );
    print( A // B,               sep = '' );
    print( numpy.mod(A, B),      sep = '' );
    print( numpy.power(A, B),    sep = '' );

