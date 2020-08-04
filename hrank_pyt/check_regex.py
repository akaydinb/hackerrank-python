#!/usr/bin/python3

import re

if __name__ == '__main__':
    for k in range(int(input())):
        try:
            re.compile( input());
            print("True");
        except re.error:
            print("False");

