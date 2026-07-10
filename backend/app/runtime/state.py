from dataclasses import dataclass, field
from typing import Any

from app.models import Message


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

    # ===== Observations =====
    observations: dict[str, Any] = field(default_factory=dict)

    # ===== Long-Term Memory =====
    long_term_memory: dict[str, Any] = field(default_factory=dict)

    # ===== Runtime Variables =====
    runtime_variables: dict[str, Any] = field(default_factory=dict)

    # ===== Environment =====
    environment: dict[str, Any] = field(default_factory=dict)