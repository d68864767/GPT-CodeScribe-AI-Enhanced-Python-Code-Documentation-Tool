```python
# analyzer.py

# Import the necessary modules
import ast
import _ast
from collections import defaultdict

class CodeAnalyzer(ast.NodeVisitor):
    """
    A class used to analyze Python code files.

    ...

    Attributes
    ----------
    functions : dict
        a dictionary to store the functions in the code and their details
    classes : dict
        a dictionary to store the classes in the code and their details
    variables : dict
        a dictionary to store the variables in the code and their details

    Methods
    -------
    visit_FunctionDef(node)
        Visits a function definition in the code and stores its details
    visit_ClassDef(node)
        Visits a class definition in the code and stores its details
    visit_Assign(node)
        Visits a variable assignment in the code and stores its details
    """

    def __init__(self):
        self.functions = defaultdict(list)
        self.classes = defaultdict(list)
        self.variables = defaultdict(list)

    def visit_FunctionDef(self, node):
        """
        Visits a function definition in the code and stores its details.

        Parameters:
        node (_ast.FunctionDef): The function definition node to visit.
        """

        self.functions[node.name].append({
            'args': [arg.arg for arg in node.args.args],
            'returns': ast.dump(node.returns) if node.returns else None,
            'docstring': ast.get_docstring(node)
        })
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """
        Visits a class definition in the code and stores its details.

        Parameters:
        node (_ast.ClassDef): The class definition node to visit.
        """

        self.classes[node.name].append({
            'bases': [base.id for base in node.bases if isinstance(base, _ast.Name)],
            'docstring': ast.get_docstring(node)
        })
        self.generic_visit(node)

    def visit_Assign(self, node):
        """
        Visits a variable assignment in the code and stores its details.

        Parameters:
        node (_ast.Assign): The assignment node to visit.
        """

        for target in node.targets:
            if isinstance(target, _ast.Name):
                self.variables[target.id].append({
                    'value': ast.dump(node.value),
                    'type': type(node.value).__name__
                })
        self.generic_visit(node)

def analyze_code(code):
    """
    Analyzes the given Python code and returns its structure.

    Parameters:
    code (str): The Python code to analyze.

    Returns:
    dict: A dictionary containing the structure of the code.
    """

    tree = ast.parse(code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)

    return {
        'functions': dict(analyzer.functions),
        'classes': dict(analyzer.classes),
        'variables': dict(analyzer.variables)
    }
```
