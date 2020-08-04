#!/usr/bin/python3

from collections import Counter
import operator

if __name__ == '__main__':
    L = [char for char in input()];
    
    #dictOfWords = { i : L.count(i)  for i in L }
    dictOfWords = Counter(L);
    print(dictOfWords)

    Keys = [ ]; Values = [ ];
    for key, value in dictOfWords():
        Keys.append(key);
        Values.append(value);
    
    for i in range(3):
        t = max(dictOfWords.items(), key = operator.itemgetter(1));
        indices = [ i for i, x in enumarate(Values) == t[1]];
        
        del dictOfWords[ t[0] ];
        