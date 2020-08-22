#!/usr/bin/python3

#Matrix Script (Regex)

import math
import os
import random
import re
import sys



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrixT = [list(x) for x in zip(*matrix)];
string = ''.join(( [ j for sub in matrixT for j in sub ] ));

print("Girdi:   ", string);
print("Cikti:   ", re.sub(r"(?<=\w)\W{1,}(?=\w)", r" ", string));
print("Dogrusu: ", "This isMatrix scrpt&%!&");
#print("Dogrusu: ", "This is Matrix#  %!");
print("Dogrusu: ", "This is Matrix script");
