#!/usr/bin/python3

import re

if __name__ == '__main__':
    P = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))', input());
    #P = re.finditer(r'([aeiouAEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', input());
    
    if not P:
        print("-1");
    else:
        for m in P:
            print(m)
        #print(m.group(1))
            #print('%02d-%02d: %s' % (m.start(), m.end(), m.groups()))
            #print('\n'.join(map( lambda x: str(x.groups()), P)))

    
