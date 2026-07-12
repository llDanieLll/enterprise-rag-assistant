from app.runtime.plan import Action, Plan
from app.runtime.state import RuntimeState
from app.toolbox import Toolbox
from app.runtime.execution_result import ExecutionResult
from app.rag.retriever import retrieve
from app.providers.base import ChatProvider
from app.providers.ollama_provider import OllamaProvider


class Executor:
    """Executes the Plan produced by the Planner.

    The Executor is responsible for carrying out a plan. It does not
    decide what to do—that responsibility belongs to the Planner.
    """

    def __init__(self, provider: ChatProvider | None = None):
        self.toolbox = Toolbox()
        # These integrations will be wired to the real implementations
        # in the next development stage.
        self.retriever = retrieve
        self.provider = provider or OllamaProvider()

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
            return ExecutionResult(
                action=plan.action,
                source="runtime",
                success=True,
                payload=plan.payload,
                reason=plan.reason,
            )

        raise ValueError(f"Unsupported action: {plan.action}")

    def _execute_tool(self, plan: Plan, state: RuntimeState):
        """Execute the requested tool and return an ExecutionResult."""

        tool_result = self.toolbox.execute_tool(
            plan.tool,
            **plan.payload,
        )

        return ExecutionResult(
            action=plan.action,
            source=plan.tool,
            success=True,
            payload=tool_result,
            reason=plan.reason,
        )

    def _execute_retrieval(self, plan: Plan, state: RuntimeState):
        """Execute a retrieval request described by the plan payload."""
        payload = plan.payload
        question = payload["query"]
        top_k = payload.get("top_k", 3)
        retrieval_result = self.retriever(question=question, top_k=top_k)

        return ExecutionResult(
            action=plan.action,
            source="retriever",
            success=True,
            payload=retrieval_result,
            reason=plan.reason,
        )

    def _execute_chat(self, plan: Plan, state: RuntimeState):
        """Execute a chat/provider request described by the plan payload."""
        payload = plan.payload
        message = payload["message"]
        context = payload.get("context")
        model = payload.get("model", state.environment.get("model"))

        chat_result = self.provider.chat(
            message=message,
            context=context if isinstance(context, list) else ([context] if context else None),
            model=model,
        )

        return ExecutionResult(
            action=plan.action,
            source="provider",
            success=True,
            payload=chat_result,
            reason=plan.reason,
        )
