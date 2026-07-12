

"""Smoke test for the Executor.

This script exercises each execution path of the Executor independently:

1. FINISH
2. TOOL
3. RETRIEVE
4. CHAT

It is intended to be run manually and is not a pytest test.
"""

from app.runtime.executor import Executor
from app.runtime.plan import Action, Plan
from app.runtime.state import RuntimeState


executor = Executor()


def run_case(name: str, plan: Plan, state: RuntimeState) -> None:
    print(f"\n{'=' * 60}")
    print(name)
    print(f"Plan Action : {plan.action.value}")

    try:
        result = executor.execute(plan, state)

        print(f"Result Action : {result.action.value}")
        print(f"Source        : {result.source}")
        print(f"Success       : {result.success}")
        print(f"Reason        : {result.reason}")
        print(f"Payload       : {result.payload}")

    except Exception as exc:
        print("Execution failed")
        print(type(exc).__name__)
        print(exc)


empty_state = RuntimeState(current_user_message="Hello")

run_case(
    "FINISH",
    Plan(
        action=Action.FINISH,
        payload={},
        reason="The task has already been completed.",
    ),
    empty_state,
)

run_case(
    "TOOL",
    Plan(
        action=Action.TOOL,
        tool="calculator",
        payload={
            "expression": "3 + 4",
        },
        reason="The request requires arithmetic.",
    ),
    empty_state,
)

run_case(
    "RETRIEVE",
    Plan(
        action=Action.RETRIEVE,
        payload={
            "query": "overall GPA",
            "top_k": 3,
        },
        reason="Retrieve relevant information.",
    ),
    RuntimeState(
        current_user_message="Calculate my overall GPA.",
        uploaded_files=["transcript.pdf"],
    ),
)

run_case(
    "CHAT",
    Plan(
        action=Action.CHAT,
        payload={
            "message": "Summarize the student's performance.",
            "context": ["Student GPA: 3.82"],
        },
        reason="Generate the final response.",
    ),
    empty_state,
)

print("\nExecutor smoke test completed.")