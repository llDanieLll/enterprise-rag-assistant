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

    def run(self, initial_state: RuntimeState) -> RuntimeState:
        """Run the runtime until the planner signals completion.

        The engine repeatedly performs single state transitions by calling
        `step()`. The planner is responsible for deciding when the task has
        finished by returning `Action.FINISH`.
        """

        state = initial_state

        while True:
            # Ask the planner whether another runtime step is required.
            plan = self.planner.plan(state)

            # Stop the runtime when the planner decides the task is complete.
            if plan.action.value == "finish":
                return state

            # Perform exactly one state transition.
            state = self.step(state)