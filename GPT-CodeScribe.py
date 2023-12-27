```python
# GPT-CodeScribe.py

# Import the necessary modules
import sys
import os
from config import INPUT_FILE_PATH, OUTPUT_FILE_PATH, INVALID_FILE_ERROR, SUCCESS_MESSAGE
from analyzer import analyze_code
from doc_generator import generate_documentation

def main():
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Please provide a Python file to generate documentation for.")
        return

    # Get the file path from the command line arguments
    file_path = sys.argv[1]

    # Check if the file exists and is a Python file
    if not os.path.isfile(file_path) or not file_path.endswith('.py'):
        print(INVALID_FILE_ERROR)
        return

    # Read the Python file
    with open(file_path, 'r') as file:
        code = file.read()

    # Analyze the Python code
    code_structure = analyze_code(code)

    # Generate the documentation
    documentation = generate_documentation(code_structure)

    # Write the documentation to a file
    output_file_path = OUTPUT_FILE_PATH + os.path.basename(file_path).replace('.py', '.md')
    with open(output_file_path, 'w') as file:
        file.write(documentation)

    print(SUCCESS_MESSAGE)

if __name__ == "__main__":
    main()
```
