#!/usr/bin/python3

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag);
        for att in attrs:
            print("->", att[0], ">", att[1]);
    def handle_endtag(self, tag):
        print("End  :", tag);
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag);
        for att in attrs:
            print("->", att[0], ">", att[1]);

if __name__ == '__main__':
    parser = MyHTMLParser();
    for _ in range(int(input())):
        parser.feed(input());

    
