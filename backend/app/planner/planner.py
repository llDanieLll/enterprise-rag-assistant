

from app.runtime.plan import Action, Plan
from app.runtime.state import RuntimeState


class Planner:
    """Rule-based planner for the AI Runtime.

    The Planner examines the current RuntimeState and decides what
    the runtime should do next. It does not execute tools or call
    the LLM directly; it only returns a Plan.
    """

    def plan(self, state: RuntimeState) -> Plan:
        """Determine the next action based on the current runtime state."""

        message = state.current_user_message.lower()

        # Rule 1: Requests that require arithmetic.
        calculation_keywords = [
            "calculate",
            "average",
            "mean",
            "sum",
            "total",
        ]

        if any(keyword in message for keyword in calculation_keywords):
            return Plan(
                action=Action.TOOL,
                tool="calculator",
                reason="The request requires arithmetic.",
            )

        # Rule 2: If documents have been uploaded, prefer retrieval.
        if state.uploaded_files:
            return Plan(
                action=Action.RETRIEVE,
                reason="Relevant information may exist in the uploaded documents.",
            )

        # Rule 3: Default to normal conversation.
        return Plan(
            action=Action.CHAT,
            reason="General conversation; no tool or retrieval required.",
        )