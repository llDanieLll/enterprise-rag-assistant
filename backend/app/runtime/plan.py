

from dataclasses import dataclass
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
    """

    action: Action
    tool: str | None = None
    reason: str = ""