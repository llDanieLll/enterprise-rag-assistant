from dataclasses import dataclass, field
from typing import Any


from app.models import Message
from app.runtime.execution_result import ExecutionResult


@dataclass
class RuntimeState:
    """
    Shared state of the AI Runtime.

    Every major runtime component (Planner, Executor, Memory,
    Provider, etc.) reads from and/or updates this object.
    """

    # ===== Conversation =====
    current_user_message: str
    conversation_history: list[Message] = field(default_factory=list)

    # ===== Retrieval =====
    uploaded_files: list[str] = field(default_factory=list)
    retrieved_chunks: list[str] = field(default_factory=list)

    # ===== Execution History =====
    # Chronological history of all execution results produced during
    # the current runtime session.
    observations: list[ExecutionResult] = field(default_factory=list)

    # ===== Long-Term Memory =====
    long_term_memory: dict[str, Any] = field(default_factory=dict)

    # ===== Runtime Context =====
    # Ephemeral variables used while the runtime is executing.
    runtime_variables: dict[str, Any] = field(default_factory=dict)

    # ===== Environment =====
    environment: dict[str, Any] = field(default_factory=dict)