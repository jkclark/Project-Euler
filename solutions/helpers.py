"""This module contains useful functions for all solutions."""
import tracemalloc
from time import time


def measure_time_and_memory(func):
    """A decorator for measuring a function's duration and memory usage."""

    def wrapper(*args, **kwargs):
        # Keep track of time elapsed and memory used
        start_time = time()
        tracemalloc.start()

        return_value = func(*args, **kwargs)

        # Stop tracking time and memory
        snapshot = tracemalloc.take_snapshot()
        end_time = time()
        tracemalloc.stop()

        # Print time elapsed and memory used
        print_time_elapsed(start_time, end_time)
        print_memory_usage_report(snapshot)

        return return_value

    return wrapper


def print_memory_usage_report(snapshot: tracemalloc.Snapshot):
    """Print the amount of memory allocated in the snapshot."""
    stats = snapshot.statistics("filename")
    print(f"Memory: {_format_bytes_humanized(stats[0].size)}")


def print_time_elapsed(start: float, end: float):
    """Print the difference between start and end, measured in seconds."""
    print(f"Time: {round(end - start, 3)}s")


def _format_bytes_humanized(num: int, suffix: str = "B") -> str:
    """Return a human-readable string representing a number of bytes."""
    for unit in ["", "Ki", "Mi"]:
        if abs(num) < 1024.0:
            return f"{round(num, 3)} {unit}{suffix}"
        num /= 1024.0
    return f"{round(num, 3)} Gi{suffix}"
