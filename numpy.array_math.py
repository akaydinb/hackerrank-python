#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    [ N, M ] = input().split();
    A = numpy.array( input().split(), int);
    B = numpy.array( input().split(), int);

    print(A);
    print(B);

    print( "[", numpy.add(A, B),      "]", sep = '' );
    print( "[", numpy.subtract(A, B), "]", sep = '' );
    print( "[", numpy.multiply(A, B), "]", sep = '' );
    print( "[", A // B,               "]", sep = '' );
    print( "[", numpy.mod(A, B),      "]", sep = '' );
    print( "[", numpy.power(A, B),    "]", sep = '' );

