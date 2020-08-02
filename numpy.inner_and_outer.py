#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    matA = numpy.array( input().split(), int);
    matB = numpy.array( input().split(), int);

    print(numpy.inner(matA, matB))
    print(numpy.outer(matA, matB))
