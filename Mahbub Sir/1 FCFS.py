import matplotlib.pyplot as plt

num_process = int(input("Number of process: "))

arrival_time = []
burst_time = []
system_idle = 0
waiting_time = []
turnaround_time = []
process_sequence = []
time_entry = []
time_exit = []
time = 0

print("Give arrival time in sequence: ")
for i in range(num_process):
    val = float(input())
    arrival_time.append(val)

print("Give burst time in sequence: ")
for i in range(num_process):
    val = float(input())
    burst_time.append(val)

for i in range(num_process):

    if time < arrival_time[i]:  # system delay calculate kore nilam
        system_idle += abs(time - arrival_time[i])
        time = arrival_time[i]

    process_sequence.append(i)
    time_entry.append(time)
    time = time + burst_time[i]
    time_exit.append(time)

for i in range(num_process):
    turnaround_time.append(time_exit[i] - arrival_time[i])
    waiting_time.append(turnaround_time[i] - burst_time[i])

print("Process Sequence = ", process_sequence)
print("Process start time ", time_entry)
print("Process finished at ", time_exit)
print("Turnaround time ", turnaround_time)
print("Waiting time ", waiting_time)

plt.barh(y=process_sequence, width=burst_time, left=time_entry)
plt.show()

'''

5
0
0
0
0
0
2
1
8
4
5

'''
