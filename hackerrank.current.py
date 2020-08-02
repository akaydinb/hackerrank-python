#!/usr/bin/python3

# Triange Quest 2 : https://www.hackerrank.com/challenges/triangle-quest-2/problem


for i in range(1, int(input())+1):
    print( *range(1, i+1) , *range(i-1, 0, -1) );
    
print( "".join(list(range(1, i+1))), "".join(list(range(i-1, 0, -1))));
