![technology Python](https://img.shields.io/badge/technology-python-blue.svg)

This application allows to extract information from a string representing a json object.

## Installation

Install dependencies: `pip install -r requirements.txt`

## Run

`python main.py`

 If you want to redirects the output of the script to filename.txt, run:

`python main.py --output filename`

 It is possible to pass other options to the CLI.

`python main.py --help`

## Question 5

> Reflecting on the technical spec you received as part of the questionnaire, how would you change it to make it less error prone (you're being asked to parse a property chain... is this the best way of doing it?) .Feel free to propose alternatives, listing pros and cons

An alternative to make it, would be obtaining a list of attributes, that way it avoids looking for a regex pattern that identifies what operation is necesary to perform.

For example:
* ["attr1", "attr2", (2), "4", 5]

Pros:
String are dictionaries ("attr1", "attr2", "4") keys and integers' set are list indexes. This makes parser easier.
Keys can have special characters included ".", "[", "]" and also can be integers.

Cons:
Lost readability. It can be confused at first glas.

