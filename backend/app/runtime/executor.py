

from app.runtime.plan import Action, Plan
from app.runtime.state import RuntimeState
from app.toolbox import Toolbox


class Executor:
    """Executes the Plan produced by the Planner.

    The Executor is responsible for carrying out a plan. It does not
    decide what to do—that responsibility belongs to the Planner.
    """

    def __init__(self):
        self.toolbox = Toolbox()

    def execute(self, plan: Plan, state: RuntimeState):
        """Execute the given plan.

        This initial implementation only dispatches actions. Actual tool,
        retrieval, and provider integrations will be added incrementally.
        """

        if plan.action == Action.TOOL:
            return self._execute_tool(plan, state)

        if plan.action == Action.RETRIEVE:
            return self._execute_retrieval(plan, state)

        if plan.action == Action.CHAT:
            return self._execute_chat(plan, state)

        if plan.action == Action.FINISH:
            return None

        raise ValueError(f"Unsupported action: {plan.action}")

    def _execute_tool(self, plan: Plan, state: RuntimeState):
        """Execute the requested tool and return a structured execution result.

        For now, the execution result is represented as a dictionary. This will
        later become an ExecutionResult dataclass.
        """

        tool_result = self.toolbox.execute_tool(
            plan.tool,
            **getattr(plan, "payload", {}),
        )

        return {
            "action": plan.action.value,
            "source": plan.tool,
            "success": True,
            "payload": tool_result,
            "reason": plan.reason,
        }

    def _execute_retrieval(self, plan: Plan, state: RuntimeState):
        """Placeholder for retrieval execution."""
        return {
            "status": "pending",
            "action": plan.action.value,
            "reason": plan.reason,
        }

    def _execute_chat(self, plan: Plan, state: RuntimeState):
        """Placeholder for LLM/provider execution."""
        return {
            "status": "pending",
            "action": plan.action.value,
            "reason": plan.reason,
        }