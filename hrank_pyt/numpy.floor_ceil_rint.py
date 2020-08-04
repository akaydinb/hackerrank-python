#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    my_array = numpy.array(input().split(), float);
    print(numpy.array2string(numpy.floor(my_array), sign = ' '))
    print(numpy.array2string(numpy.ceil(my_array), sign = ' '))
    print(numpy.array2string(numpy.rint(my_array), sign = ' '))

