

from dataclasses import dataclass, field
from typing import Any
from enum import Enum


class Action(Enum):
    """High-level actions that the Planner can request."""

    CHAT = "chat"
    RETRIEVE = "retrieve"
    TOOL = "tool"
    FINISH = "finish"


@dataclass
class Plan:
    """A structured execution plan produced by the Planner.

    The Planner decides *what* should happen next by creating a Plan.
    The Executor is responsible for carrying out that plan.
    A Plan is the formal contract between the Planner and the Executor. It
    describes what action should be executed, together with any parameters
    required to perform that action.
    """

    action: Action
    tool: str | None = None
    # Parameters required by the selected action. For example, tool arguments,
    # retrieval queries, or generation options.
    payload: dict[str, Any] = field(default_factory=dict)
    reason: str = ""