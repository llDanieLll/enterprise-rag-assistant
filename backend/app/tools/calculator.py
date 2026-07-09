"""
calculator.py

The Calculator tool performs basic arithmetic calculations.

This tool is intentionally simple for the first version of the AI Agent.
Later it can be extended to support symbolic math, unit conversions,
and more advanced numerical operations.
"""


def calculator(expression: str) -> dict:
    """
    Evaluate a mathematical expression.

    Args:
        expression: A mathematical expression such as
                    "25 * (8 + 2)".

    Returns:
        A standardized observation dictionary.
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})

        return {
            "tool": "calculator",
            "success": True,
            "observation": result,
        }

    except Exception as e:
        return {
            "tool": "calculator",
            "success": False,
            "observation": str(e),
        }
