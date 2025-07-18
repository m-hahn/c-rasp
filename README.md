# Interpreter for C-RASP

This is an interpreter for [C-RASP](https://arxiv.org/abs/2404.04393) programs, written in Python.

## Installation

```
pip install -r requirements.txt
```

## Usage

Write a C-RASP grammar and save it to a file. An example is in [dyck1_yc24.cr](https://github.com/coli-saar/c-rasp/blob/main/dyck1_yc24.cr)
(this is the program for Dyck languages with one type of brackets from Yang & Chiang 2024).

Run the interpreter as follows. Tokens are specified in a whitespace-separated string on the command line.

```
python crasp.py -c dyck1_yc24.cr "( ( ) ( ) )" --tracing html --trace-file trace.html
```

## Tracing

The interpreter will print `True` or `False` to the command line, depending on whether the last position of the final expression
evaluated to true or not. We interpret this as the program accepting the input tokens.

You can also save a trace of the intermediate results in a file. Specify `--tracing html` or `--tracing txt` to save the trace in
a HTML file containing a table or a plain text file, and specify the filename with the `--trace-file` option. The trace file will
show the list of variable assignments with their new values as they happen.

