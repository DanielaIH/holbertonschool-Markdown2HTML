#!/usr/bin/python3
"""
This is a script markdown2html.py
that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
"""


from sys import argv
from os import path
import markdown

if __name__ == "__main__":
    """main program"""
    if len(argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if len(argv) >= 2:
        if not path.exists(argv[1]):
            print("Missing " + argv[1])
            exit(1)
        with open(argv[1], "r") as f:
            markdown = markdown.markdown(f.read())
        with open(argv[2], "w") as f:
            f.write(markdown)
        exit(0)
