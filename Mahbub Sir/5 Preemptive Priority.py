import matplotlib.pyplot as plt

num_process = int(input("Number of process: "))
process = []

for i in range(num_process):
    print("process :", i)
    process_id = i
    arrival = int(input())
    burst = int(input())
    priority = int(input())
    entry_time = -1
    exit_time = -1
    work_done = 0
    data = [process_id, arrival, burst, priority, entry_time, exit_time, work_done]
    process.append(data)

process.sort(key=lambda x: x[3], reverse=True)

timeline = [-1 for i in range(500)]
start = 0
for i in range(num_process):
    cnt = 0
    start = process[i][1]
    while cnt < process[i][2]:
        while timeline[start] != -1:
            start += 1
        if timeline[start] == -1:
            timeline[start] = process[i][0]
            process[i][5] = start + 1
            cnt += 1
        start += 1

timeline = timeline[0:start]

turnaround_time = []
waiting_time = []

process.sort(key=lambda x: x[0])
for i in range(num_process):
    turnaround_time.append(process[i][5] - process[i][1])
    waiting_time.append(turnaround_time[i] - process[i][2])

print("Process          = ", timeline)
print("Timeline         = ", [i + 1 for i in range(len(timeline))])
print("Turnaround Time  = ", turnaround_time)
print("Waiting Time     = ", waiting_time)

'''

3
0
4
4
2
4
10
3
2
1

'''
