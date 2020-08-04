#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    [ N, M ] = input().split();
    print(numpy.array2string(numpy.eye(int(N), int(M)), sign = ' '))
