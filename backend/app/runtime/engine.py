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

        The engine repeatedly performs planning, execution, and state
        transitions while printing a development trace of each iteration.
        """

        state = initial_state
        iteration = 1

        while True:
            print("\n" + "=" * 60)
            print(f"Iteration {iteration}")
            print("=" * 60)

            # Ask the planner for the next action.
            plan = self.planner.plan(state)

            print(f"Planner Action : {plan.action.value}")
            print(f"Reason         : {plan.reason}")

            if getattr(plan, "tool", None):
                print(f"Tool           : {plan.tool}")

            if getattr(plan, "payload", None):
                print(f"Payload        : {plan.payload}")

            # Stop if the planner decides the task is complete.
            if plan.action.value == "finish":
                print("\nAgent execution completed.")
                return state

            # Execute the current plan.
            result = self.executor.execute(plan, state)

            print(f"Executor Source: {result.source}")
            print(f"Success        : {result.success}")
            print(f"Observation    : {result.payload}")

            # Transition to the next runtime state.
            state = self.state_manager.transition(state, result)

            print("State updated.")

            iteration += 1