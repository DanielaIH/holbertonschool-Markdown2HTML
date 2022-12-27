#!/usr/bin/python3
'''
This is a script markdown2html.py
that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
'''

from sys import argv, stderr
from os import path


def markdown2html():
    """main program"""
    import markdown
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html\n", file=stderr)
        exit(1)
    if not path.exists(argv[1]):
        print("Missing {}\n".format(argv[1]), file=stderr)
        exit(1)
    with open(argv[1], "r") as f:
        markdownvar = markdown.markdown(f.read())
    with open(argv[2], "w") as f:
        f.write(markdownvar + "\n")
    exit(0)


if __name__ == "__main__":
    markdown2html()
