def calculate_metrics(results):
    if not results:
        raise ValueError("results cannot be empty")

    n = len(results)

    avg_waiting = sum(r["waiting"] for r in results) / len(results)
    avg_turnaround = sum(r["turnaround"] for r in results) / len(results)
    busy_time = sum(r["burst"] for r in results)       # total CPU work done
    total_time = max(r["completion"] for r in results)      # when the last process finished
    cpu_utilization = busy_time / total_time * 100

    return {
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround,
        "cpu_utilization": cpu_utilization,
    }