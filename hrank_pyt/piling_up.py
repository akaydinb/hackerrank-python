#!/usr/bin/python3

# Piling Up!
from collections import deque

if __name__ == '__main__':
    for T in range(int(input())):
        n = int(input());
        L = list(map(int, input().split()));
        D = deque(L);
        L.sort(reverse = True);

        for k in range(n):
            if L[k] == D[-1]:
                D.pop();
            elif L[k] == D[0]:          
                D.popleft();
            else:
                print("No");
                break;
            
            if len(D) <= 2:
                print("Yes");
                break;
            
#################################
            ##ind, M = max(enumerate(L), key = operator.itemgetter(1));
            #RM1 = L.pop();
            #if ( RM1 < L[-1] ):
                #print("No");
                #break;
            
            #LM1 = L.popleft();
            #if ( LM1 < L[0] ):
                #print("No");
                #break;
            
            #if ( len(L) == 2):
                #print("Yes");
                #break;
            #else:
                #n = len(L);
            
            
#################################
            #M = max(L);
            ##print("maxelement = ", M);
            ##input();
            #if L[0] == M:
                ##L.pop(0);
                #L.popleft();
                #n = n - 1;
            #elif L[-1] == M:
                ##L.pop(-1);
                #L.pop();
                #n = n - 1;
            #else:
                #print("No");
                #break;

            #if len(L) == 2:
                #print("Yes");
                #break;