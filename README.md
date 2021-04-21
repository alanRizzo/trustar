![technology Python](https://img.shields.io/badge/technology-python-blue.svg)

This application allows to extract information from a string representing a json object.

## Installation

Install dependencies: `pip install -r requirements.txt`

## Run

`python main.py`

 If you want to redirects the output of the script to output.txt, run:

`python main.py > output.txt`

## Question 5

> Reflecting on the technical spec you received as part of the questionnaire, how would you change it to make it less error prone (you're being asked to parse a property chain... is this the best way of doing it?) .Feel free to propose alternatives, listing pros and cons

An alternative to make it, would be obtaining a list of attributes, that way it avoids looking for a pattern that identifies what operation is necesary to perform.

For example:
* ["attr1", "attr2", 2]
String are dictionaries keys and integers are list indexes.

