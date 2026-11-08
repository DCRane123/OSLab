from oslab.cpu.process import Process
from oslab.cpu.fcfs import fcfs

def test_fcfs_basic() :
    processes = [Process("P1", 0, 5), Process("P2", 1, 3)]
    results, gantt = fcfs(processes)
    assert results[1]["completion"] == 8

def test_fcfs_idle_gap():
    processes = [Process("P1", 0, 2),Process("P2", 5, 2)]
    results, gantt = fcfs(processes)
    assert results[1]["start"] == 5
    assert results[1]["completion"] == 7
    assert results[1]["waiting"] == 0

    assert gantt == [("P1", 0, 2),("P2", 5, 7)]