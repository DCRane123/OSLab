from oslab.cpu.process import Process
from oslab.cpu.sjf import sjf
from oslab.cpu.metrics import calculate_metrics

def test_sjf():
    processes = [Process("P1", 0, 7), Process("P2", 2, 4), Process("P3", 4, 1), Process("P4", 5, 4)]
    results, gantt = sjf(processes)

    assert gantt == [
        ("P1", 0, 7),
        ("P3", 7, 8),
        ("P2", 8, 12),
        ("P4", 12, 16)
    ]
    metrics = calculate_metrics(results)
    assert metrics["avg_waiting"] == 4.0

def test_sjf_idle_gap():
    processes = [Process("P1", 0, 2), Process("P2", 5, 2)]
    results, gantt = sjf(processes)
    assert gantt == [("P1", 0, 2), ("P2", 5, 7)]


def test_sjf_tie_break_ignores_input_order():
    processes = [Process("P1", 0, 7), Process("P4", 5, 4),
                 Process("P2", 2, 4), Process("P3", 4, 1)]
    results, gantt = sjf(processes)
    assert gantt == [("P1", 0, 7), ("P3", 7, 8), ("P2", 8, 12), ("P4", 12, 16)]