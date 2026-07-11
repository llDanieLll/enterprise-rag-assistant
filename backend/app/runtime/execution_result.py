"""Execution result model.

This module defines the contract between the Executor and the future
StateManager. Every execution (tool call, retrieval, or chat generation)
returns an ExecutionResult describing what happened.
"""

from dataclasses import dataclass
from typing import Any

from app.runtime.plan import Action


@dataclass
class ExecutionResult:
    """Represents the outcome of executing a single plan.

    Attributes:
        action: The action that was executed.
        source: The component or tool that produced the result
                (e.g. "calculator", "retriever", "provider").
        success: Whether the execution completed successfully.
        payload: The raw output returned by the executed component.
        error: Optional error message when execution fails.
        reason: Planner reasoning associated with this execution.
    """

    action: Action
    source: str
    success: bool
    payload: Any
    error: str | None = None
    reason: str = ""
