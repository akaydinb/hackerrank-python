#!/usr/bin/python3

# This is not completed yet
import numpy

if __name__ == '__main__':
    dims = tuple(map(int, input().split()));
    
    print(numpy.zeros((dims), dtype = numpy.int));
    print(numpy.ones((dims), dtype = numpy.int));
