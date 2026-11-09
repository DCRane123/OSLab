def srtf(processes):
    # Reset, so running srtf twice on the same list gives the same answer
    for p in processes:
        p.remaining_time = p.burst_time

    first_start = {}   # pid -> first time it got the CPU (for response time)
    completion = {}    # pid -> time it finished
    gantt = []
    current_time = 0

    # Loop until every process has a completion time
    while len(completion) < len(processes):
        # Processes that have arrived and still have work left
        ready = [p for p in processes
                 if p.arrival_time <= current_time and p.remaining_time > 0]

        # Nobody ready: CPU is idle, so jump to the next arrival
        if not ready:
            current_time = min(p.arrival_time for p in processes
                               if p.remaining_time > 0)
            continue

        # Smallest remaining time wins; ties go to the earlier arrival
        chosen = min(ready, key=lambda p: (p.remaining_time, p.arrival_time))

        # Remember the first time this process touches the CPU
        if chosen.pid not in first_start:
            first_start[chosen.pid] = current_time

        # Merge this 1-unit slice into the previous Gantt segment if possible
        if gantt and gantt[-1][0] == chosen.pid and gantt[-1][2] == current_time:
            gantt[-1] = (chosen.pid, gantt[-1][1], current_time + 1)
        else:
            gantt.append((chosen.pid, current_time, current_time + 1))

        # Run the chosen process for 1 time unit
        chosen.remaining_time -= 1
        current_time += 1

        if chosen.remaining_time == 0:
            completion[chosen.pid] = current_time

    # Build results in the same format as FCFS and SJF
    results = []
    for p in processes:
        ct = completion[p.pid]
        turnaround = ct - p.arrival_time
        waiting = turnaround - p.burst_time
        response = first_start[p.pid] - p.arrival_time
        results.append({
            "pid": p.pid,
            "arrival": p.arrival_time,
            "burst": p.burst_time,
            "start": first_start[p.pid],
            "completion": ct,
            "turnaround": turnaround,
            "waiting": waiting,
            "response": response,
        })

    return results, gantt