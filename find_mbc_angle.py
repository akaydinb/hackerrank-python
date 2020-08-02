#!/usr/bin/python3

import math

if __name__ == '__main__':

    AB = int(input());
    BC = int(input());

    print( round(math.atan2(AB, BC) * 180.0 / math.pi), u'\N{DEGREE SIGN}', sep = '' )

