
def fcfs(processes):
    processes = sorted(processes, key=lambda p: p.arrival_time)

    current_time = 0
    results = []
    gantt = []

    for p in processes:
        start = max(current_time, p.arrival_time)
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

    return results, gantt