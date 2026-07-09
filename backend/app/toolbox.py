"""
toolbox.py

The Toolbox manages all tools that are available to the AI Agent.

Responsibilities:
1. Register available tools.
2. Describe available tools to the LLM.
3. Retrieve a tool by name.
4. (Future) Execute a selected tool.
"""

from app.tools.calculator import calculator
from app.tools.calender import calendar
from app.tools.filesystem import filesystem
from app.tools.pdf_search import pdf_search
from app.tools.python_executor import python_executor
from app.tools.sql_database import sql_database
from app.tools.web_search import web_search

try:
    from app.memory import memory
except ImportError:
    memory = None

try:
    from app.email_sender import email_sender
except ImportError:
    email_sender = None


class Toolbox:
    """Registry of all tools available to the AI Agent."""

    def __init__(self):
        self.tools = {
            "calculator": {
                "function": calculator,
                "description": "Perform mathematical calculations.",
            },
            "calendar": {
                "function": calendar,
                "description": "Retrieve calendar and date information.",
            },
            "filesystem": {
                "function": filesystem,
                "description": "Read files from the local filesystem.",
            },
            "pdf_search": {
                "function": pdf_search,
                "description": "Search uploaded PDF documents.",
            },
            "python_executor": {
                "function": python_executor,
                "description": "Execute safe Python expressions.",
            },
            "sql_database": {
                "function": sql_database,
                "description": "Query a SQL database.",
            },
            "web_search": {
                "function": web_search,
                "description": "Search the web for current information.",
            },
        }

        if memory is not None:
            self.tools["memory"] = {
                "function": memory,
                "description": "Store and retrieve long-term memory.",
            }

        if email_sender is not None:
            self.tools["email_sender"] = {
                "function": email_sender,
                "description": "Send emails on behalf of the user.",
            }

    def list_tools(self) -> list[dict]:
        """Return the name and description of every registered tool."""
        return [
            {
                "name": name,
                "description": tool["description"],
            }
            for name, tool in self.tools.items()
        ]

    def get_tool(self, name: str):
        """Return the function associated with a tool name."""
        tool = self.tools.get(name)
        if tool is None:
            return None
        return tool["function"]