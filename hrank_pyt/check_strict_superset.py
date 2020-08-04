#!/usr/bin/python3

if __name__ == '__main__':
    A = set( input().split() );
    S = list( );
    for _ in range(int(input())):
        N = set( input().split() );
        S.append( (A != N) and N.issubset(A) );

    print(all(S))    
