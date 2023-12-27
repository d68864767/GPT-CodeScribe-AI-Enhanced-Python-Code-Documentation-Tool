```python
# cli.py

import argparse
from GPT-CodeScribe import main
from config import DEFAULT_VERBOSITY, VERBOSITY_LEVELS, INVALID_VERBOSITY_ERROR

def create_parser():
    # Create the parser
    parser = argparse.ArgumentParser(description="Generate detailed and informative documentation for Python code using GPT-CodeScribe.")

    # Add the arguments
    parser.add_argument('FilePath', metavar='filepath', type=str, help='the path to the Python file to document')
    parser.add_argument('-v', '--verbosity', type=str, choices=VERBOSITY_LEVELS, default=DEFAULT_VERBOSITY, help='the level of detail in the generated documentation (default: %(default)s)')

    return parser

def validate_args(args):
    # Check if the verbosity level is valid
    if args.verbosity not in VERBOSITY_LEVELS:
        print(INVALID_VERBOSITY_ERROR)
        return False

    return True

def run():
    # Create the argument parser
    parser = create_parser()

    # Parse the command line arguments
    args = parser.parse_args()

    # Validate the arguments
    if not validate_args(args):
        return

    # Run the main function with the provided arguments
    main(args.FilePath, args.verbosity)

if __name__ == "__main__":
    run()
```
