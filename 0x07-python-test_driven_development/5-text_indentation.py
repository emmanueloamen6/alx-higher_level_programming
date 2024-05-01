#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""

def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
       """print text delim."""
       text = (delim + "\n\n").join(
               [line.strip(" ") for line in text.split(delim)])
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

