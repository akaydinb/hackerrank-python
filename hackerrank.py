#!/usr/bin/python3

from itertools import combinations

def minion_game(string):
    stuart = set();
    kevin  = set();
#    for i in range(len(string)):
#        for j in range(i, len(string)):
#            substr = string[i:j+1];
#            if substr[0] in ['A', 'E', 'I', 'O', 'U']:
#                kevin.add(substr);
#            else:
#                stuart.add(substr);
    substr = set( string[x:y] for x, y in combinations(range(len(string) + 1), r = 2) );
    for astr in substr:
        if astr[0] in ['A', 'E', 'I', 'O', 'U']:
            kevin.add(astr);
        else:
            stuart.add(astr);

    Spoints = 0;
    Kpoints = 0;
    
    print(stuart);
    print(kevin);
    
    for x in stuart:
        print("[", Spoints, "]", x, string.count(x));
        Spoints = Spoints + string.count(x);

#https://stackoverflow.com/questions/37499968/finding-all-repeated-substrings-in-a-string-and-how-often-they-appear
#https://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches

    for x in kevin:
        print("[", Kpoints, "]", x, string.count(x));
        Kpoints = Kpoints + string.count(x);
        
    if Spoints > Kpoints:
        print("Stuart", Spoints);
    elif Kpoints > Spoints:
        print("Kevin", Kpoints);
    elif Spoints == Kpoints:
        print("Draw");

if __name__ == '__main__':
    s = input();
    minion_game(s);
