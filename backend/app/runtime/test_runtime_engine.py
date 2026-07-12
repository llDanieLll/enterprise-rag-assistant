

"""End-to-end integration test for RuntimeEngine.

This script starts with a single RuntimeState and lets the RuntimeEngine
perform planning, execution, and state transitions until the planner
returns FINISH.

Run manually:

    python -m app.runtime.test_runtime_engine
"""

from app.runtime.engine import RuntimeEngine
from app.runtime.state import RuntimeState


def main() -> None:
    print("=" * 60)
    print("RuntimeEngine Integration Test")
    print("=" * 60)

    engine = RuntimeEngine()

    initial_state = RuntimeState(
        current_user_message="Calculate my overall GPA from the uploaded transcript.",
        uploaded_files=["transcript.pdf"],
    )

    final_state = engine.run(initial_state)

    print("\n" + "=" * 60)
    print("Final Runtime Summary")
    print("=" * 60)

    print(f"Observations      : {len(final_state.observations)}")
    print(f"Retrieved Chunks  : {len(final_state.retrieved_chunks)}")
    print(f"Runtime Variables : {final_state.runtime_variables}")

    if final_state.observations:
        last = final_state.observations[-1]
        print("\nLast Observation")
        print("-" * 60)
        print(f"Action  : {last.action.value}")
        print(f"Source  : {last.source}")
        print(f"Success : {last.success}")
        print(f"Payload : {last.payload}")

    print("\nRuntime integration test completed.")


if __name__ == "__main__":
    main()