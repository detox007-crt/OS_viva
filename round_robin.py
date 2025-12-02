# Round Robin CPU Scheduling Algorithm

processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]
burst_time = [5, 4, 2, 1]

time_quantum = 2  # Define time quantum

n = len(processes)
remaining_bt = burst_time.copy()
finish_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

time = 0
queue = []

# Initialize ready queue
for i in range(n):
    if arrival_time[i] <= time:
        queue.append(i)

# Round Robin Execution
while queue:
    i = queue.pop(0)
    
    if remaining_bt[i] > time_quantum:
        time += time_quantum
        remaining_bt[i] -= time_quantum
    else:
        time += remaining_bt[i]
        remaining_bt[i] = 0
        finish_time[i] = time  # FT when completed

    # Add new processes to queue
    for j in range(n):
        if arrival_time[j] <= time and j not in queue and remaining_bt[j] > 0 and j != i:
            queue.append(j)

    # Re-add incomplete process
    if remaining_bt[i] > 0:
        queue.append(i)

# Calculate TAT & WT
for i in range(n):
    turnaround_time[i] = finish_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Display Results
print("Process\tAT\tBT\tFT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{finish_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Average times
print("\nAverage Turnaround Time:", sum(turnaround_time) / n)
print("Average Waiting Time:", sum(waiting_time) / n)
