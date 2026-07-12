"""Utility functions used by the rule-based Planner.

These helpers inspect the RuntimeState and answer small questions about the
current execution. They intentionally do not make planning decisions; they
provide facts that the Planner can use when constructing a Plan.
"""

from app.runtime.plan import Action
from app.runtime.state import RuntimeState


CALCULATION_KEYWORDS = {
    "calculate",
    "average",
    "mean",
    "sum",
    "total",
}


def calculation_required(message: str) -> bool:
    """Return True if the user request appears to require arithmetic."""
    message = message.lower()
    return any(keyword in message for keyword in CALCULATION_KEYWORDS)


def retrieval_required(state: RuntimeState) -> bool:
    """Return True if uploaded documents exist but have not yet been retrieved."""
    print(f"The uploaded files we have: {state.uploaded_files}")
    return bool(state.uploaded_files) and not state.retrieved_chunks


def latest_action(state: RuntimeState) -> Action | None:
    """Return the most recent executed action, if any."""
    if not state.observations:
        return None
    return state.observations[-1].action


def action_completed(state: RuntimeState, action: Action) -> bool:
    """Return True if the specified action has already completed successfully."""
    return any(
        observation.action == action and observation.success
        for observation in state.observations
    )


def retrieval_completed(state: RuntimeState) -> bool:
    return action_completed(state, Action.RETRIEVE)


def chat_completed(state: RuntimeState) -> bool:
    return action_completed(state, Action.CHAT)


def tool_completed(state: RuntimeState, tool_name: str) -> bool:
    return any(
        observation.action == Action.TOOL
        and observation.success
        and observation.source == tool_name
        for observation in state.observations
    )


def latest_observation(state: RuntimeState):
    if not state.observations:
        return None
    return state.observations[-1]


def task_completed(state: RuntimeState) -> bool:
    return chat_completed(state)