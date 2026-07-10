

"""Runtime engine.

The RuntimeEngine orchestrates a single iteration of the AI runtime. It does
not implement planning, execution, or state transitions itself; instead, it
coordinates the Planner, Executor, and StateManager.
"""

from app.planner.planner import Planner
from app.runtime.executor import Executor
from app.runtime.state import RuntimeState
from app.runtime.state_manager import StateManager


class RuntimeEngine:
    """Coordinates the runtime execution pipeline."""

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.state_manager = StateManager()

    def step(self, state: RuntimeState) -> RuntimeState:
        """Execute a single runtime iteration.

        Pipeline:
            RuntimeState
                ↓
            Planner
                ↓
              Plan
                ↓
            Executor
                ↓
        ExecutionResult
                ↓
          StateManager
                ↓
        Next RuntimeState
        """

        plan = self.planner.plan(state)
        result = self.executor.execute(plan, state)
        next_state = self.state_manager.transition(state, result)

        return next_state