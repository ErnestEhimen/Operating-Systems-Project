#Richard Ketiku First come first serve Algorithm
# Step 1: Create the number of processes
num_processes = int(input("Enter the number of processes: "))
processes = []

# Step 2: Get the ID and Service time for each process
for i in range(num_processes):
    pid = input(f"Enter the process ID for process {i+1}: ")
    service_time = int(input(f"Enter the service time for process {i+1}: "))
    processes.append({'pid': pid, 'service_time': service_time})

# Step 3: Initialize the waiting time of the first process to zero
waiting_time = [0]

# Step 4: Calculate the Total time and Processing time for the remaining processes
total_time = [processes[0]['service_time']]
for i in range(1, num_processes):
    processing_time = total_time[i-1] + waiting_time[i-1]
    total_time.append(processing_time + processes[i]['service_time'])

    # Step 5: Calculate the waiting time for the current process
    wait_time = total_time[i-1]
    waiting_time.append(wait_time)

# Step 6: Calculate the total turnaround time for each process
turnaround_time = []
for i in range(num_processes):
    turnaround_time.append(total_time[i] - waiting_time[i])

# Step 7: Calculate the total waiting time for all processes
total_waiting_time = sum(waiting_time)
# Step 8: Calculate the total turnaround time for all processes
total_turnaround_time = sum(turnaround_time)
# Step 9: Calculate the average waiting time
avg_waiting_time = total_waiting_time / num_processes
# Step 10: Calculate the average turnaround time
avg_turnaround_time = total_turnaround_time / num_processes
print(f"Average waiting time: {avg_waiting_time}")
print(f"Average turnaround time: {avg_turnaround_time}")
