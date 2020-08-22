#!/usr/bin/python3

def minion_game(string):
    Spoints = 0;
    Kpoints = 0;

    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            Kpoints = Kpoints + len(string) - i;
        else:
            Spoints = Spoints + len(string) - i;
    
    if Spoints > Kpoints:
        print("Stuart", Spoints);
    elif Kpoints > Spoints:
        print("Kevin", Kpoints);
    elif Spoints == Kpoints:
        print("Draw");
    
if __name__ == '__main__':
    s = input();
    minion_game(s);
