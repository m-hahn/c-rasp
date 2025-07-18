import argparse
import sys

from fasttext_pybind import args

from program import *
from parser import parse_file
from tracing import TraceToFile, TraceToHTML


def parse_args():
    parser = argparse.ArgumentParser(description="Run a C-RASP program.")

    # Mandatory: c-rasp program file
    parser.add_argument(
        "-c", "--c-rasp-file",
        type=str,
        help="Path to the C-RASP program file"
    )

    # Mandatory: tokens from command-line argument
    parser.add_argument(
        "tokens",
        help="Whitespace-separated list of tokens (e.g. '( ( ) )')"
    )

    # Optional: tracing type
    parser.add_argument(
        "--tracing",
        choices=["txt", "html"],
        help="Tracing output type (txt or html)"
    )

    # Conditionally required: trace filename
    parser.add_argument(
        "--trace-file",
        help="Filename for tracing output (required if --trace-type is given)"
    )

    args = parser.parse_args()

    # Enforce: if trace-type is given, trace-file must be given
    if args.tracing and not args.trace_file:
        parser.error("--trace-file is required when --tracing is specified")

    return args


args = parse_args()
program = parse_file(args.c_rasp_file)
tokens = args.tokens.split(" ")

# tokens = "(()())"

if args.tracing == "txt":
    with TraceToFile(args.trace_file) as tr:
        print(program.execute(tokens, tracing=tr))
    print(f"Trace written to {args.trace_file}")

elif args.tracing == "html":
    with TraceToHTML(args.trace_file) as tr:
        print(program.execute(tokens, tracing=tr))
    print(f"Trace written to {args.trace_file}")

else:
    print(program.execute(tokens))