import pytest
from oslab.cpu.process import Process

def test_process_creation() :
    p = Process("P1", 0, 5)
    assert p.pid == "P1"
    assert p.arrival_time == 0
    assert p.burst_time == 5

def test_negative_arrival_time() :
    with pytest.raises(ValueError):
        Process("P1", -1, 5)

def test_negative_burst_time() :
    with pytest.raises(ValueError) :
        Process("P1", 0, -5)

def test_zero_burst_time() :
    with pytest.raises(ValueError) :
        Process("P1", 0, 0)

def test_empty_pid_raises_error() :
    with pytest.raises(ValueError) :
        Process("", 0, 5)
