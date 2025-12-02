# Non-preemptive Priority Scheduling

def priority_scheduling(processes):
    n = len(processes)
    
    # Sort processes based on priority (lower number = higher priority)
    processes.sort(key=lambda x: x['priority'])

    time = 0
    for p in processes:
        p['start'] = time
        p['finish'] = time + p['bt']
        p['tat'] = p['finish'] - p['at']
        p['wt'] = p['tat'] - p['bt']
        time += p['bt']

    return processes


# Input Section
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    print(f"\nEnter details for Process P{i+1}")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    priority = int(input("Priority (lower = higher): "))
    processes.append({'pid': f'P{i+1}', 'at': at, 'bt': bt, 'priority': priority})

# Run Scheduling
result = priority_scheduling(processes)

# Output
print("\n===== Non-Preemptive Priority Scheduling Results =====")
print("PID\tAT\tBT\tPriority\tFT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['priority']}\t\t{p['finish']}\t{p['tat']}\t{p['wt']}")

# Average Times
avg_tat = sum(p['tat'] for p in result) / n
avg_wt = sum(p['wt'] for p in result) / n
print("\nAverage Turnaround Time:", round(avg_tat, 2))
print("Average Waiting Time:", round(avg_wt, 2))
