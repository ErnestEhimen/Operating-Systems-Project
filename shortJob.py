# define a function to sort the list of processes by their service time
def sort_by_service_time(processes):
    return sorted(processes, key=lambda x: x[1])

# get the number of processes
num_processes = int(input("Enter the number of processes: "))

# get the ID and service time for each process
processes = []
for i in range(num_processes):
    pid = input("Enter process ID: ")
    service_time = int(input("Enter service time for process {}: ".format(pid)))
    processes.append((pid, service_time))

# sort the list of processes by their service time (SJF algorithm)
processes = sort_by_service_time(processes)

# calculate the waiting time and total time for each process
waiting_times = [0]
total_times = [processes[0][1]]
for i in range(1, num_processes):
    waiting_time = total_times[i-1]
    waiting_times.append(waiting_time)
    
    service_time = processes[i][1]
    total_time = waiting_time + service_time
    total_times.append(total_time)

# calculate the total waiting time, total turnaround time, average waiting time, and average turnaround time
total_waiting_time = sum(waiting_times)
total_turnaround_time = sum(total_times)
avg_waiting_time = total_waiting_time / num_processes
avg_turnaround_time = total_turnaround_time / num_processes

print("Total waiting time: {}".format(total_waiting_time))
print("Total turnaround time: {}".format(total_turnaround_time))
print("Average waiting time: {}".format(avg_waiting_time))
print("Average turnaround time: {}".format(avg_turnaround_time))