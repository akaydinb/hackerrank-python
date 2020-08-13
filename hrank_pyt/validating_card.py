#!/usr/bin/python3

# Validating Credit Card Numbers
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        I = input();

#        print(any( [ bool(re.search(r"^[4-6]\d{15}", I)),
#                     bool(re.search(r"^[4-6]\d{3}-\d{4}-\d{4}-\d{4}", I)) ]));        
#                     bool(re.search(r"(\d)\1{3,}", re.sub("-", "", I)))  ]));

        if bool(re.search(r"^[4-6]\d{15}$", I)) or bool(re.search(r"^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$", I)):
            if bool(re.search(r"^[4-6]\d*(\d)\1{3,}", re.sub("-", "", I))):
                print(I, "\tInvalid");
            else:
                print(I, "\tValid");
        else:
            print(I, "\tInvalid");
                
#        print( bool(re.search("\d*(\d)\1{2,}\d*", re.sub("-", "", I)) ));
#        print( operator.not_(bool(re.search(r"(\d)\1{3,}", re.sub("-", "", I)) )));

#        print(any( [ bool(re.search("^\+\d*\.\d+$", I)),
#                     bool(re.search("^\-\d*\.\d+$", I)),
#                     bool(re.search("^\d*\.\d+$", I)),
#                     bool(re.search("^\.\d+$", I))]))
