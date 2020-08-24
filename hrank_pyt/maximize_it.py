#!/usr/bin/python3

#Maximize It! 
import itertools

def square(number):
    return (number ** 2)

def modulo(L, M):
    return [ item % M for item in L ];

if __name__ == '__main__':
    [ K, M ] = map(int, input().split());
    
    L = [ ];    
    for _ in(range(K)):
        #girdi = map(int, input().split());
        #L.append(modulo(list(map(square, girdi)), M));
        L.append( list(map(square, map(int, input().split())))[1:]  );

    #print(L)
        
    en_buyuk = 0;
    for X in itertools.product(*L):
        sX = sum(X) % M;
        #print(en_buyuk, sX, X);
        if sX > en_buyuk:
            en_buyuk = sX;
    
    print(en_buyuk);
