"""
agent.py

The Agent is the "brain" of the system.

Responsibilities:
1. Receive the user's question.
2. Decide whether a tool is needed.
3. Execute the selected tool.
4. Return the final answer.

For now, the decision is rule-based.
Later, it will be replaced by an LLM.
"""


class Agent:
    def __init__(self):
        pass

    def decide(self, question: str) -> str:
        """
        Decide which tool to use.

        Returns:
            "pdf_search" -> Search uploaded PDFs
            "none" -> Answer directly
        """

        question = question.lower()

        pdf_keywords = [
            "pdf",
            "document",
            "file",
            "resume",
            "certificate",
        ]

        if any(keyword in question for keyword in pdf_keywords):
            return "pdf_search"

        return "none"

    def execute(self, tool: str, question: str):
        """
        Execute the selected tool.

        This is only a placeholder.
        Actual tool implementations will be added later.
        """

        if tool == "pdf_search":
            return {
                "tool": tool,
                "result": "PDF search placeholder",
            }

        return {
            "tool": "none",
            "result": None,
        }

    def run(self, question: str):
        """
        Main entry point of the Agent.
        """

        tool = self.decide(question)

        observation = self.execute(tool, question)

        return observation