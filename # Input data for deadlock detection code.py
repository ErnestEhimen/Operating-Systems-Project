# Input data
num_processes = 3
num_resources = 3
max_matrix = [[3, 6, 8], [4, 3, 3], [3, 4, 4]]
allocation_matrix = [[3, 3, 3], [2, 0, 3], [1, 2, 4]]
available_resources = [1, 2, 0]

# Initialize data structures
work = available_resources.copy()
finish = [False] * num_processes
deadlock_processes = []

# Check for deadlock for each process
for i in range(num_processes):
    if not finish[i]:
        can_be_allocated = True
        for j in range(num_resources):
            if allocation_matrix[i][j] > work[j]:
                can_be_allocated = False
                break
        if can_be_allocated:
            finish[i] = True
            deadlock_processes.append(f'P{i}')
            for j in range(num_resources):
                work[j] += allocation_matrix[i][j]
                
# Check if there are any deadlock processes
if len(deadlock_processes) == 0:
    print("No deadlock detected.")
else:
    print("System is in deadlock and deadlock processes are: ")
    print(", ".join(deadlock_processes))
