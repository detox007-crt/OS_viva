# FCFS CPU Scheduling Algorithm

# Sample Input (You can modify this)
processes = ['P1', 'P2', 'P3']
arrival_time = [0, 2, 4]
burst_time = [5, 3, 2]

# Initialize lists
finish_time = [0] * len(processes)
turnaround_time = [0] * len(processes)
waiting_time = [0] * len(processes)

# Compute finish time
current_time = 0
for i in range(len(processes)):
    if current_time < arrival_time[i]:
        current_time = arrival_time[i]  # CPU Idle time
    current_time += burst_time[i]
    finish_time[i] = current_time

# Compute turnaround time and waiting time
for i in range(len(processes)):
    turnaround_time[i] = finish_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Display results
print("Process\tAT\tBT\tFT\tTAT\tWT")
for i in range(len(processes)):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{finish_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Average waiting and turnaround time
print("\nAverage Turnaround Time:", sum(turnaround_time)/len(processes))
print("Average Waiting Time:", sum(waiting_time)/len(processes))
