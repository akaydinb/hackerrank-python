#!/usr/bin/python3

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        #people.sort(key = operator.itemgetter(2));
        people = sorted(people, key = lambda x: int(operator.itemgetter(2)(x)))
        print(people);
        x = [ ];
        for theguy in people:
            x.append(f( theguy ))
            
        print(x)
        return x

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
    

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


#######################################################################
#def wrapper(f):    f = sortphone
#    def fun(l):    l = liste sort_phone'a giren argument
#        for k in range(len(l)):
#            if len(l[k]) == 10:
#                l[k] = '+91 '+l[k][0:5]+" "+l[k][5:10];
#            elif len(l[k]) == 12:
#                l[k] = '+91 '+l[k][2:7]+" "+l[k][7:12];
#            elif l[k][0:3] == '+91':
#                l[k] = l[k][0:3]+" "+l[k][3:8]+" "+l[k][8:]
#            elif l[k][0] == '0':
#                l[k] = '+91 '+l[k][1:6]+" "+l[k][6:]
##        f(l);     = sort_phone(l)
#    return fun

#@wrapper
#def sort_phone(l):
#    print(*sorted(l), sep='\n')
#
#if __name__ == '__main__':
#    l = [input() for _ in range(int(input()))]
#    sort_phone(l) 



