

"""
python_executor.py

The Python Executor tool executes simple Python expressions and
returns the execution result as an observation.

This is the first version and is intentionally limited.
Later versions will execute generated Python code in a controlled
sandbox instead of using eval().
"""


def python_executor(expression: str) -> dict:
    """
    Execute a simple Python expression.

    Args:
        expression: A Python expression to evaluate.

    Returns:
        A standardized observation dictionary.
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})

        return {
            "tool": "python_executor",
            "success": True,
            "observation": result,
        }

    except Exception as e:
        return {
            "tool": "python_executor",
            "success": False,
            "observation": str(e),
        }