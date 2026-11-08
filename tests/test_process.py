from oslab.cpu.process import process

def test_process_creation() :
    p = process("P1", 0, 5)
    assert p.pid == "P1"
    assert p.arrival_time == 0
    assert p.burst_time == 5
