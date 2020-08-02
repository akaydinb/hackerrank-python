#!/usr/bin/python3

def print_formatted(number):
    L = len(bin(number)) - 2;
    fstr = "{0:" + str(L) + "d} {0:" + str(L) + "o} {0:" + str(L) + "X} {0:" + str(L) + "b}"

    for k1 in range(number):
        k2 = k1 + 1;
        print(fstr.format(k2))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
