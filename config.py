```python
# config.py

# Import the os module
import os

# GPT API Key
GPT_API_KEY = os.getenv('GPT_API_KEY')

# Default verbosity level for the generated documentation
DEFAULT_VERBOSITY = 'medium'

# Error messages
INVALID_FILE_ERROR = "Invalid file. Please provide a valid Python file."
INVALID_VERBOSITY_ERROR = "Invalid verbosity level. Please choose between 'low', 'medium', or 'high'."

# Success messages
SUCCESS_MESSAGE = "Documentation generated successfully."

# File handling
INPUT_FILE_PATH = "input/"
OUTPUT_FILE_PATH = "output/"

# Customization options
VERBOSITY_LEVELS = ['low', 'medium', 'high']
```
