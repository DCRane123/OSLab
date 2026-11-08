
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
