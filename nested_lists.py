#!/usr/bin/python


if __name__ == '__main__':

    students = [ ];

    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students.append( [ name, score ] );
    
    # https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
    sorted_students = sorted(students, key = lambda x: x[1])

    minnote = sorted_students[0][1];
    while sorted_students[0][1] == minnote:
        sorted_students.pop(0);    # remove the lowest value to make second lowest value the lowest

    minnote = sorted_students[0][1]; finallist = [ ];
    for anyelement in sorted_students:
        if anyelement[1] == minnote:
            finallist.append(anyelement[0]);

    finallist.sort()

    for anyelement in finallist:
        print anyelement

