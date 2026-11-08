import pytest
from oslab.cpu.process import Process
from oslab.cpu.fcfs import fcfs
from oslab.cpu.metrics import calculate_metrics


def test_metrics_idle_gap():
    processes = [Process("P1", 0, 2), Process("P2", 5, 2)]
    results, gantt = fcfs(processes)
    metrics = calculate_metrics(results)
    assert metrics["avg_waiting"] == 0.0
    assert metrics["avg_turnaround"] == 2.0
    assert metrics["cpu_utilization"] == pytest.approx(57.14, abs=0.01)


def test_metrics_empty_raises_error():
    with pytest.raises(ValueError):
        calculate_metrics([])