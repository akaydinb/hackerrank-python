#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    coeff = numpy.array( input().split(), float );

    print(numpy.polyval(coeff, int(input())));
