

"""Smoke test for the RuntimeEngine.

This is a temporary architectural smoke test. Its purpose is to verify that a
single runtime state transition can complete successfully.
"""

from app.runtime.engine import RuntimeEngine
from app.runtime.state import RuntimeState


def main() -> None:
    """Run one runtime step and inspect the resulting state."""

    state = RuntimeState(
        current_user_message="Hello Runtime"
    )

    engine = RuntimeEngine()

    print("=" * 60)
    print("Initial RuntimeState")
    print("=" * 60)
    print(state)

    try:
        print("\nExecuting one runtime step...")
        next_state = engine.step(state)
    except Exception as exc:
        print("\nSmoke test failed!")
        print(f"Exception: {type(exc) .__name__}: {exc}")
        raise

    print("\n" + "=" * 60)
    print("Next RuntimeState")
    print("=" * 60)
    print(next_state)

    print("\nObservation count:", len(next_state.observations))
    if next_state.observations:
        print("Latest observation:")
        print(next_state.observations[-1])

    print("\nSmoke test completed successfully.")


if __name__ == "__main__":
    main()