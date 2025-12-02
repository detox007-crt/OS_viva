# Preemptive Priority Scheduling Algorithm

def preemptive_priority_scheduling(processes):
    n = len(processes)
    time = 0
    completed = 0
    executed_time = [0] * n
    is_completed = [False] * n

    while completed != n:
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            if processes[i]['at'] <= time and not is_completed[i]:
                if processes[i]['priority'] < highest_priority:
                    highest_priority = processes[i]['priority']
                    idx = i
                # If priority is same, choose process with smaller arrival time
                if processes[i]['priority'] == highest_priority:
                    if processes[i]['at'] < processes[idx]['at']:
                        idx = i

        if idx != -1:
            executed_time[idx] += 1
            time += 1

            # If process is completed
            if executed_time[idx] == processes[idx]['bt']:
                processes[idx]['finish'] = time
                processes[idx]['tat'] = processes[idx]['finish'] - processes[idx]['at']
                processes[idx]['wt'] = processes[idx]['tat'] - processes[idx]['bt']
                is_completed[idx] = True
                completed += 1
        else:
            time += 1  # If no process is available at this time
            
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
result = preemptive_priority_scheduling(processes)

# Output
print("\n===== Preemptive Priority Scheduling Results =====")
print("PID\tAT\tBT\tPriority\tFT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['priority']}\t\t{p['finish']}\t{p['tat']}\t{p['wt']}")

# Average Times
avg_tat = sum(p['tat'] for p in result) / n
avg_wt = sum(p['wt'] for p in result) / n
print("\nAverage Turnaround Time:", round(avg_tat, 2))
print("Average Waiting Time:", round(avg_wt, 2))
