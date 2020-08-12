#!/usr/bin/python3

# Company Logo

from collections import Counter
from operator import itemgetter

if __name__ == '__main__':
    L = [char for char in input()];
    
    dictOfWords = Counter(L);

    tekrarlar = list(dictOfWords.values());
    harfler = list(dictOfWords.keys());
    
    #print( (sorted(zip(tekrarlar, harfler), reverse=True)[:3]))
    
    #for element in sorted(zip(tekrarlar, harfler), reverse=True)[:3]:
    #    print(element[1], element[0]);
    
    #print( *(zip(harfler, tekrarlar) ));
    L = [ list(a) for a in zip(harfler, tekrarlar) ];
    
    
    ###################
    s = sorted(L, key = itemgetter(1), reverse = True);
    print(s);
    s = sorted(s, key = itemgetter(0));
    print(s);
    for i, j in s[:3]:
        print(i, j);
    ###################
    
    
#    for i, j in sorted(L, key = lambda x: (x[1], x[0]), reverse=True)[:3]:
#        print(i, j);



# @moose, @Amyth, to reverse to only one attribute, you can sort twice: 
# first by the secondary s = sorted(s, key = operator.itemgetter(2)) then 
# by the primary s = sorted(s, key = operator.itemgetter(1), reverse=True) 
# Not ideal, but works. – tomcounsell Apr 13 '15 at 9:43 
# Stackoverflow, sort a list by multiple attributes
