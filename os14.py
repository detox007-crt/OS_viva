def is_safe(processes, available, max_need, allocation):
    n = len(processes)
    m = len(available)

    finish = [False] * n
    safe_sequence = []
    need = []

    # Calculate Need matrix
    for i in range(n):
        need.append([max_need[i][j] - allocation[i][j] for j in range(m)])
    
    print("\nNeed Matrix:")
    for i in range(n):
        print(f"P{i}: {need[i]}")
    
    # Banker's algorithm
    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= available[j] for j in range(m)):
                    print(f"\nProcess P{i} is executing...")
                    available = [available[j] + allocation[i][j] for j in range(m)]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    found = True
                    print(f"Available after P{i} execution: {available}")
        
        if not found:
            print("\nSystem is in unsafe state! Deadlock possible.")
            return None
    
    print("\nSystem is in SAFE STATE")
    return safe_sequence


# Input Section
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix:")
allocation = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]

print("\nEnter Maximum Need Matrix:")
max_need = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

processes = [f"P{i}" for i in range(n)]

# Run Banker's Algorithm
safe_seq = is_safe(processes, available, max_need, allocation)

# Output
if safe_seq:
    print("\nSafe Sequence:", " → ".join(safe_seq))
