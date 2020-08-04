#!/usr/bin/python3

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data: 
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data);
 
    def handle_data(self, data):
        if "\n" not in data:
            print(">>> Data")
            print(data)

#    def handle_starttag(self, tag, attrs):
#        print("Start :", tag);
#        for att in attrs:
#            print("->", att[0], ">", att[1]);
#    def handle_endtag(self, tag):
#        print("End  :", tag);
#    def handle_startendtag(self, tag, attrs):
#        print("Empty :", tag);
#        for att in attrs:
#            print("->", att[0], ">", att[1]);

if __name__ == '__main__':
    #parser = MyHTMLParser();
    #for _ in range(int(input())):
    #    parser.feed(input());
    html = ""       
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
    
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

    
