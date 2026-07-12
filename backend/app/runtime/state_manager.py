"""Runtime state transition manager.

The StateManager is responsible for generating the next RuntimeState from the
current RuntimeState and an ExecutionResult. It is the only component that
owns runtime state transitions.
"""

from dataclasses import replace

from app.runtime.execution_result import ExecutionResult
from app.runtime.state import RuntimeState


class StateManager:
    """Generates the next runtime state after an execution."""

    def transition(
        self,
        current_state: RuntimeState,
        result: ExecutionResult,
    ) -> RuntimeState:
        """Return the next RuntimeState.

        Version 1 performs a simple immutable state transition by copying the
        current state, appending the latest execution result to the observation
        history, and returning the new state.
        """

        observations = list(current_state.observations)
        observations.append(result)

        runtime_variables = dict(current_state.runtime_variables)
        runtime_variables["last_action"] = result.action.value
        runtime_variables["last_source"] = result.source
        runtime_variables["last_success"] = result.success
        runtime_variables["last_payload"] = result.payload

        retrieved_chunks = list(current_state.retrieved_chunks)
        long_term_memory = dict(current_state.long_term_memory)

        # Persist retrieved document chunks so the planner knows retrieval
        # has already completed.
        if result.source == "retriever" and isinstance(result.payload, list):
            retrieved_chunks = result.payload

        # Persist successful tool outputs for future planner decisions.
        elif result.source == "calculator":
            long_term_memory["calculator"] = result.payload

        # Persist the final chat response.
        elif result.source == "provider":
            long_term_memory["chat"] = result.payload

        return replace(
            current_state,
            observations=observations,
            retrieved_chunks=retrieved_chunks,
            long_term_memory=long_term_memory,
            runtime_variables=runtime_variables,
        )
