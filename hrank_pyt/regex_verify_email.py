#!/usr/bin/python3

import email.utils
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        IN = input();
        PA = email.utils.parseaddr(IN);
        RE = re.search(r"^([a-zA-Z][\w.-]*)@([a-zA-Z-]+)\.([a-zA-Z]{1,3})$", PA[1]);
        if RE is not None:
            print(RE.groups());

