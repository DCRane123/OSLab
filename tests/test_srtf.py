from oslab.cpu.process import Process
from oslab.cpu.srtf import srtf


def make_example():
    return [Process("P1", 0, 8), Process("P2", 1, 4),
            Process("P3", 2, 2), Process("P4", 3, 1)]


def test_srtf_worked_example():
    results, gantt = srtf(make_example())
    assert gantt == [("P1", 0, 1), ("P2", 1, 2), ("P3", 2, 4),
                     ("P4", 4, 5), ("P2", 5, 8), ("P1", 8, 15)]
    by_pid = {r["pid"]: r for r in results}
    assert by_pid["P1"]["completion"] == 15
    assert by_pid["P2"]["waiting"] == 3
    assert by_pid["P4"]["waiting"] == 1
    
def test_srtf_idle_gap():
    processes = [Process("P1", 0, 2), Process("P2", 5, 2),]
    results, gantt = srtf(processes)
    assert gantt == [("P1", 0, 2), ("P2", 5, 7)]

def test_srtf_run_twice():
    processes = make_example()
    result1, gantt1 = srtf(processes)
    result2, gantt2 = srtf(processes)

    assert gantt1 == gantt2