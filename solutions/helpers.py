import tracemalloc


def _format_bytes_humanized(num: int, suffix: str = 'B') -> str:
    for unit in ['', 'Ki', 'Mi']:
        if abs(num) < 1024.0:
            return f'{round(num, 3)} {unit}{suffix}'
        num /= 1024.0
    return f'{round(num, 3)} Gi{suffix}'


def print_memory_usage_report(snapshot: tracemalloc.Snapshot, line_breakdown: int = 0):
    stats = snapshot.statistics('filename')
    print(f'Memory: {_format_bytes_humanized(stats[0].size)}')

    if line_breakdown:
        print(f'{line_breakdown} most expensive line{"" if line_breakdown == 1 else "s"}:')
        stats = snapshot.statistics('lineno')
        for stat in stats[:line_breakdown]:
            print(f'  {str(stat.traceback).split(":")[-1]}: {_format_bytes_humanized(stat.size)}')


def print_time_elapsed(start: float, end: float):
    print(f'Time: {round(end - start, 3)}s')
