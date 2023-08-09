from matplotlib import pyplot as plt

num_process = int(input("Number of process: "))
quantum = int(input("Quantum value: "))

process = []

for i in range(num_process):
    print("process :", i)
    process_id = i
    arrival = float(input())
    burst = float(input())
    entry_time = -1
    exit_time = -1
    work_done = 0
    data = [process_id, arrival, burst, entry_time, exit_time, work_done]
    process.append(data)

process.sort(key=lambda x: x[1])

time = 0.0
process_schedule = []
waiting_time = []
turnaround_time = []
system_idle = 0

while True:
    for i in range(num_process):
        if time < process[i][1]:
            system_idle += abs(time - process[i][1])
            time = process[i][1]

        if process[i][2] - process[i][5] < quantum:
            dif = process[i][2] - process[i][5]
            process[i][5] += dif
            if dif > 0:
                time += dif
                process_schedule.append(str(process[i][0]) + " = " + str(time))
                process[i][4] = time
        else:
            process[i][5] += quantum
            time += quantum
            process_schedule.append(str(process[i][0]) + " = " + str(time))
            process[i][4] = time

    flag = True
    for i in range(num_process):
        if process[i][5] != process[i][2]:
            flag = False
    if flag:
        break

print(process_schedule)
for i in range(num_process):
    turnaround_time.append(process[i][4] - process[i][1])
    print("Process ", process[i][0], " turnaround time", turnaround_time[i])
    waiting_time.append(turnaround_time[i] - process[i][2])
    print("Process ", process[i][0], " waiting time", waiting_time[i])

'''
5
2
0
2
0
1
0
8
0
4
0
5

5
2
0
5
0
3
0
1
0
7
0
4
'''
