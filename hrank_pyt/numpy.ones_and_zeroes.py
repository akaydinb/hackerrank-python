#!/usr/bin/python3

# This is not completed yet
import numpy

if __name__ == '__main__':
    [N, M, P] = input().split();
    
    T0 = [ ];
    T1 = [ ];
    
    for _ in range(int(N)):
        M0 = [ ];
        M1 = [ ];
        for _ in range(int(M)):
            V0 = [ ];
            V1 = [ ];
            for _ in range(int(P)):
                V0.append(0);
                V1.append(1);
            M0.append(V0);
            M1.append(V1);
        T0.append(M0);
        T1.append(M1);
    
    print(numpy.array(T0, int))
    print(numpy.array(T1, int))
                
