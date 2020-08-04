#!/usr/bin/python3

import numpy

if __name__ == '__main__':
    [ N, M ] = input().split();
    #A = numpy.array( input().split(), int);
    #B = numpy.array( input().split(), int);
    A = [ ];
    for _ in range(int(N)):
        A.append( input().split() );

    my_array = numpy.array(A, int);
    print( numpy.array2string(numpy.mean(my_array, axis = 1), sign = ' ') );
    print( numpy.array2string(numpy.var(my_array, axis = 0), sign = ' ') );
    print("%1.11f" %numpy.std(my_array) ); 

 
