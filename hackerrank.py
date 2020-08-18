#!/usr/bin/python3

def minion_game(string):
    stuart = set();
    kevin  = set();
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            substr = string[i:j+1];
            if substr[0] in ['A', 'E', 'I', 'O', 'U']:
                kevin.add(substr);
            else:
                stuart.add(substr);
                
    Spoints = 0;
    Kpoints = 0;
    
    print(stuart);
    print(kevin);
    
    for x in stuart:
        print("[", Spoints, "]", x, string.count(x));
        Spoints = Spoints + string.count(x);
        
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