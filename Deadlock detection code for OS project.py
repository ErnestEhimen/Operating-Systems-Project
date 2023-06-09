# Initialize the matrices and vectors
n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources instances: "))

max_matrix = []
allocation_matrix = []
available_resources = []

for i in range(n):
    print(f"Enter the maximum resource allocation for process P{i}: ")
    max_row = list(map(int, input().split()))
    max_matrix.append(max_row)

for i in range(n):
    print(f"Enter the resource allocation for process P{i}: ")
    allocation_row = list(map(int, input().split()))
    allocation_matrix.append(allocation_row)

print("Enter the available resources: ")
available_resources = list(map(int, input().split()))

# Calculate the need matrix
need_matrix = []
for i in range(n):
    need_row = [max_matrix[i][j] - allocation_matrix[i][j] for j in range(m)]
    need_matrix.append(need_row)

# Initialize the finish vector
finish = [False] * n

# Initialize the work vector to the available resources
work = available_resources.copy()

# Look for an unfinished process that can be executed
while True:
    found = False
    for i in range(n):
        if not finish[i]:
            if all(need_matrix[i][j] <= work[j] for j in range(m)):
                found = True
                # Release the allocated resources
                for j in range(m):
                    work[j] += allocation_matrix[i][j]
                # Mark the process as finished
                finish[i] = True
                break
    if not found:
        break

# Check if there are any unfinished processes
if all(finish):
    print("The system is in a safe state.")
else:
    print("The system is deadlocked. The following processes are deadlocked: ")
    for i in range(n):
        if not finish[i]:
            print(f"P{i}", end=" ")
