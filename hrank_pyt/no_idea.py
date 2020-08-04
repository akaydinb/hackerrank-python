#!/usr/bin/python3

import collections

if __name__ == '__main__':
    
    [n, m] = input().split();
    E = list( input().split());
    A = set( input().split());
    B = set( input().split());

    dictE = collections.Counter(E);
    sumA = 0;
    sumB = 0;

    for k in A:
        sumA = sumA + int(dictE[k]);

    for k in B:
        sumB = sumB + int(dictE[k]);

    print(abs(sumA - sumB))
#    print( len(E.intersection(A)) - len(E.intersection(B)));


    
