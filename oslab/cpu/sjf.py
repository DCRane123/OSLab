def sjf(processes):
    remaining = processes.copy()

    current_time = 0
    results = []
    gantt = []

    while remaining:
        available = [p for p in remaining if p.arrival_time <= current_time]
        if not available:
            current_time = min(p.arrival_time for p in remaining)
            continue
        p = min(available, key=lambda p: (p.burst_time, p.arrival_time))

        start = current_time
        completion = start + p.burst_time
        turnaround = completion - p.arrival_time
        waiting = turnaround - p.burst_time
        response = start - p.arrival_time

        results.append({
            "pid": p.pid,
            "arrival": p.arrival_time,
            "burst": p.burst_time,
            "start": start,
            "completion": completion,
            "turnaround": turnaround,
            "waiting": waiting,
            "response": response
        })

        gantt.append((p.pid, start, completion))

        current_time = completion
        remaining.remove(p)

    return results, gantt
