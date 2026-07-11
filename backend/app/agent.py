"""
agent.py

Version 1 of the AI Agent.

Current responsibilities:
1. Own a Toolbox instance.
2. Ask the Toolbox which tools are available.
3. Build a tool-selection prompt for the LLM.

Tool execution will be added in the next iteration.
"""

from app.toolbox import Toolbox
from openai import OpenAI


class Agent:
    """The decision-making component of the AI Agent."""

    def __init__(self):
        self.toolbox = Toolbox()
        self.client = OpenAI()

    def available_tools(self) -> list[dict]:
        """Return metadata describing every available tool."""
        return self.toolbox.list_tools()

    def build_tool_selection_prompt(self, user_question: str) -> str:
        """Construct the prompt that asks the LLM to choose a tool."""

        tool_descriptions = self.available_tools()

        tools_text = "\n".join(
            f"- {tool['name']}: {tool['description']}"
            for tool in tool_descriptions
        )

        prompt = f"""
You are an AI agent.

Available tools:
{tools_text}

User question:
{user_question}

Choose the single best tool for solving the user's request.
Return ONLY the tool name.
""".strip()

        return prompt

    def select_tool(self, user_question: str) -> str:
        """Ask the LLM to choose the best tool for the user's request."""

        prompt = self.build_tool_selection_prompt(user_question)

        response = self.client.responses.create(
            model="gpt-5.5",
            input=prompt,
        )

        tool_name = response.output_text.strip()

        return tool_name