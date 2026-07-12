

from app.runtime.plan import Action, Plan
from app.runtime.state import RuntimeState
from app.planner.planner_utils import (
    calculation_required,
    retrieval_required,
    retrieval_completed,
    tool_completed,
    task_completed,
)


class Planner:
    """Rule-based planner for the AI Runtime.

    The Planner examines the current RuntimeState and decides what
    the runtime should do next. It does not execute tools or call
    the LLM directly; it only returns a Plan.
    """

    def plan(self, state: RuntimeState) -> Plan:
        """Determine the next action based on the current runtime state."""
        # The planner decides *what* to do next. State inspection is delegated
        # to planner_utils so that this method focuses purely on decision making.

        # Rule 0: Finish if the runtime has already produced a final response.
        # This is a placeholder termination rule and will later be replaced by
        # an LLM-based planning decision.
        if task_completed(state):
            return Plan(
                action=Action.FINISH,
                payload={},
                reason="The task has already been completed.",
            )

        # Rule 1: Retrieve required information before executing tools.
        if retrieval_required(state):
            return Plan(
                action=Action.RETRIEVE,
                payload={
                    "query": state.current_user_message,
                },
                reason="Relevant information may exist in the uploaded documents.",
            )

        # Rule 2: Execute the calculator only after the required information
        # has been gathered, and only if it has not already run.
        if (
            calculation_required(state.current_user_message)
            and not tool_completed(state, "calculator")
        ):
            return Plan(
                action=Action.TOOL,
                tool="calculator",
                payload={
                    "expression": "3 + 4",
                    # this state_current_user_message is hard_coded as 3+4
                },
                reason="The request requires arithmetic.",
            )

        # Rule 3: Once retrieval or tool execution has completed, generate
        # the final response.
        if retrieval_completed(state) or tool_completed(state, "calculator"):
            return Plan(
                action=Action.CHAT,
                payload={
                    "message": state.current_user_message,
                    "context": state.retrieved_chunks,
                },
                reason="Enough information has been gathered to generate the final response.",
            )

        # Rule 4: Default to normal conversation.
        return Plan(
            action=Action.CHAT,
            payload={
                "message": state.current_user_message,
            },
            reason="General conversation; no tool or retrieval required.",
        )