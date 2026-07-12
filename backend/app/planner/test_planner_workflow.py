

"""Planner workflow smoke test.

This script exercises the Planner by constructing several RuntimeState
instances that represent different stages of an agent workflow.

Expected workflow:

State 0 -> RETRIEVE
State 1 -> TOOL
State 2 -> CHAT
State 3 -> FINISH
"""

from app.planner.planner import Planner
from app.runtime.execution_result import ExecutionResult
from app.runtime.plan import Action
from app.runtime.state import RuntimeState


planner = Planner()


def run_case(name: str, state: RuntimeState, expected: Action) -> None:
    """Execute one planner test case."""

    print(f"\n{'=' * 60}")
    print(name)
    print(f"Expected : {expected.value}")

    plan = planner.plan(state)

    print(f"Actual   : {plan.action.value}")
    print(f"Reason   : {plan.reason}")
    print(f"Payload  : {plan.payload}")

    if plan.action == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")


run_case(
    "State 0 - Retrieval Required",
    RuntimeState(
        current_user_message="Calculate my overall GPA.",
        uploaded_files=["transcript.pdf"],
    ),
    Action.RETRIEVE,
)

run_case(
    "State 1 - Tool Required",
    RuntimeState(
        current_user_message="Calculate my overall GPA.",
        uploaded_files=["transcript.pdf"],
        retrieved_chunks=["Course list and grades"],
        observations=[
            ExecutionResult(
                action=Action.RETRIEVE,
                source="retriever",
                success=True,
                payload={},
                reason="Retrieval completed.",
            )
        ],
    ),
    Action.TOOL,
)

run_case(
    "State 2 - Generate Final Response",
    RuntimeState(
        current_user_message="Calculate my overall GPA.",
        uploaded_files=["transcript.pdf"],
        retrieved_chunks=["Course list and grades"],
        observations=[
            ExecutionResult(Action.RETRIEVE, "retriever", True, {}, ""),
            ExecutionResult(Action.TOOL, "calculator", True, {"gpa": 3.82}, ""),
        ],
    ),
    Action.CHAT,
)

run_case(
    "State 3 - Finish",
    RuntimeState(
        current_user_message="Calculate my overall GPA.",
        uploaded_files=["transcript.pdf"],
        retrieved_chunks=["Course list and grades"],
        observations=[
            ExecutionResult(Action.RETRIEVE, "retriever", True, {}, ""),
            ExecutionResult(Action.TOOL, "calculator", True, {"gpa": 3.82}, ""),
            ExecutionResult(Action.CHAT, "provider", True, {}, "Final response generated."),
        ],
    ),
    Action.FINISH,
)

print("\nPlanner workflow smoke test completed.")