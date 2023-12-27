# GPT-CodeScribe: AI-Enhanced Python Code Documentation Tool

## Project Introduction and Purpose

GPT-CodeScribe is a Python script that leverages GPT (Generative Pre-trained Transformer) technology to generate detailed and informative documentation for Python code. The script analyzes Python code files and produces human-readable documentation that includes descriptions, explanations, and usage instructions. This project aims to simplify the process of generating comprehensive code documentation, making it easier for developers to understand and utilize Python code effectively.

## Installation Instructions

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set your GPT API key as an environment variable named `GPT_API_KEY`.

## Usage Guide with Examples

You can use GPT-CodeScribe from the command line as follows:

```bash
python cli.py <filepath> [-v verbosity]
```

Where:
- `<filepath>` is the path to the Python file you want to document.
- `-v` or `--verbosity` is an optional argument to set the level of detail in the generated documentation. It can be 'low', 'medium', or 'high'. The default is 'medium'.

For example:

```bash
python cli.py my_script.py -v high
```

This will generate high-detail documentation for the Python file `my_script.py`.

## Customization Options

You can customize the level of detail in the generated documentation by using the `-v` or `--verbosity` command line argument. The available options are 'low', 'medium', and 'high'.

## How GPT-CodeScribe Works

GPT-CodeScribe works in three main steps:

1. **Python Code Analysis:** The script reads the provided Python file and analyzes its structure, functions, and variables using the `analyzer.py` module.
2. **Documentation Generation:** The script uses the GPT model to generate documentation based on the analyzed code structure. This is done in the `doc_generator.py` module.
3. **Output:** The generated documentation is printed to the console and also saved to a file in the `output/` directory.

## Acknowledgments and Credits

This project uses the GPT model provided by OpenAI.

## Contribution Guidelines

If you want to contribute to this project, please create a new branch and submit a pull request.

## License Information

This project is licensed under the MIT License.

## Testing and Validation

The `test.py` file contains unit tests for the project. You can run the tests by executing `python -m unittest test.py`.

## Security Measures

GPT-CodeScribe does not store or transmit your code. The GPT API key is stored as an environment variable for security.

## Error Handling

The script includes error handling for invalid file paths and invalid verbosity levels.

## Continuous Improvement

We plan to continuously improve and update GPT-CodeScribe to enhance the quality and accuracy of the generated documentation. Your feedback is welcome.

## User Feedback

Please submit feedback and issues on the project's GitHub page.
</filepath>