#!/usr/bin/python3

from itertools import combinations_with_replacement

if __name__ == '__main__':
    [string, key] = input().split();
    for k in list(combinations_with_replacement(sorted(string), int(key))):
        print(''.join(k));

