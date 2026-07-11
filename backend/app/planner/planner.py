

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

        # Rule 0: Finish if the runtime has already produced a final response.
        # This is a placeholder termination rule and will later be replaced by
        # an LLM-based planning decision.
        if state.runtime_variables.get("finished", False):
            return Plan(
                action=Action.FINISH,
                reason="The task has already been completed.",
            )

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

        # Rule 2: Retrieve from uploaded documents only if retrieval has not
        # already been performed during this runtime session.
        if state.uploaded_files and not state.retrieved_chunks:
            return Plan(
                action=Action.RETRIEVE,
                reason="Relevant information may exist in the uploaded documents.",
            )

        # Rule 3: If retrieval has already been completed, continue with normal
        # conversation (later this may become tool use or answer generation).
        if state.retrieved_chunks:
            return Plan(
                action=Action.CHAT,
                reason="Relevant context has already been retrieved.",
            )

        # Rule 4: Default to normal conversation.
        return Plan(
            action=Action.CHAT,
            reason="General conversation; no tool or retrieval required.",
        )