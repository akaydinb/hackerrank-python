#!/usr/bin/python3

# Listedeki duplike elemanların count'larıyla bir dict oluşturma örneği
from collections import Counter

if __name__ == '__main__':
    L = [ ]; 
    for _ in range(int(input())):
        string_input = input();
        L.append( string_input );
    
    #dictOfWords = { i : L.count(i)  for i in L }
    dictOfWords = Counter(L);
    print(len(dictOfWords))
    
    
    for k in dictOfWords.values():
        print(k, end = ' ')
    
