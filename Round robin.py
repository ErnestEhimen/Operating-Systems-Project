class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.wait_time = 0
        self.turnaround_time = 0

    def __str__(self):
        return f"Process {self.pid}: burst_time={self.burst_time} arrival_time={self.arrival_time}"

def round_robin(processes, time_quantum):
    n = len(processes)
    ready_queue = []
    count = 0
    for i in range(n):
        ready_queue.append(processes[i])
    while ready_queue:
        process = ready_queue.pop(0)
        if process.remaining_time <= time_quantum:
            count += process.remaining_time
            process.turnaround_time = count - process.arrival_time
            process.wait_time = process.turnaround_time - process.burst_time
            process.remaining_time = 0
        else:
            count += time_quantum
            process.remaining_time -= time_quantum
            ready_queue.append(process)
        if process.remaining_time > 0:
            ready_queue.append(process)
    total_wait_time = sum([p.wait_time for p in processes])
    total_turnaround_time = sum([p.turnaround_time for p in processes])
    avg_wait_time = total_wait_time / n
    avg_turnaround_time = total_turnaround_time / n
    print(f"Average waiting time = {avg_wait_time}")
    print(f"Average turnaround time = {avg_turnaround_time}")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter the time quantum: "))
    processes = []
    for i in range(n):
        pid = f"P{i+1}"
        burst_time = int(input(f"Enter the burst time for {pid}: "))
        arrival_time = int(input(f"Enter the arrival time for {pid}: "))
        processes.append(Process(pid, burst_time, arrival_time))
    round_robin(processes, time_quantum)
