#!/usr/bin/python3

if __name__ == '__main__':
    number_of_groups = int(input());
    L = list(map(int, input().split()));
    S = set(L);
    print(int((number_of_groups * sum(S) - sum(L)) / (number_of_groups - 1)))

