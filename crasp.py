import argparse
import sys

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
        nargs="?",
        default=None,
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

if args.tokens is not None:
    input_iterable = [args.tokens]
else:
    input_iterable = sys.stdin

# tokens = args.tokens.strip().split()

# tokens = "(()())"

tr = None
if args.tracing == "txt":
    tr = TraceToFile(args.trace_file)
elif args.tracing == "html":
    tr = TraceToHTML(args.trace_file)

input_id = 1
for line in input_iterable:
    if not line.startswith("//"):
        tokens = line.strip().split()
        if len(tokens) > 0:
            result = program.execute(tokens, tracing=tr)
            print(f"{input_id} {line.strip()}: {result}")
            input_id += 1

if tr is not None:
    tr.close()
    print(f"Trace written to {args.trace_file}")

