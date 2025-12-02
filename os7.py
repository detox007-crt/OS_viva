# Non-Preemptive Shortest Job First Scheduling Algorithm

processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 2, 4, 5]
burst_time = [7, 4, 1, 4]

n = len(processes)
completed = [False] * n
finish_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

current_time = 0
completed_count = 0

while completed_count < n:
    # Find process with shortest burst time that has arrived
    idx = -1
    min_bt = float('inf')

    for i in range(n):
        if arrival_time[i] <= current_time and not completed[i] and burst_time[i] < min_bt:
            min_bt = burst_time[i]
            idx = i

    if idx == -1:  # If no process has arrived, move time forward
        current_time += 1
        continue

    current_time += burst_time[idx]
    finish_time[idx] = current_time
    completed[idx] = True
    completed_count += 1

# Calculate TAT and WT
for i in range(n):
    turnaround_time[i] = finish_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Display Results
print("Process\tAT\tBT\tFT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{finish_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Averages
print("\nAverage Turnaround Time:", sum(turnaround_time) / n)
print("Average Waiting Time:", sum(waiting_time) / n)
