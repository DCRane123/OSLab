class process :
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        
        if arrival_time < 0 :
            raise ValueError("arrival_time cannot be negative.")
        
        if burst_time <= 0 :
            raise ValueError("burst_time must be positive (greater than 0).")
        
        if not pid :
            print("Process id cannot be empty.")
            
        if pid == "" :
            print("Inavalid Process id.")
            
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        