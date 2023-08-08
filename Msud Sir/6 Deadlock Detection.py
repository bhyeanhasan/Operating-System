import numpy as np


def detection_algorithm(Allocation, Max, Available):
    Work = Available
    n = len(Allocation)
    Finish = [False for i in range(n)]  # প্রথমে সবগুলা প্রসেস ইনকম্পিট
    Need = np.subtract(Max, Allocation)  # এলোকেশনের পর আর কত রিসোর্স দরকার

    process_done = []
    process_incomplete = n

    while True:
        if process_incomplete <= 0:  # যদি সবগুলো প্রসেস কমপ্লিট হয়ে যায় তাহলে সেফ
            print("Safe State")
            for i in process_done:
                print("Process ", i, ">\n")
            break

        flag = True

        for i in range(n):
            if Finish[i] == False and all(
                    np.less_equal(Need[i], Work)):  # যদি প্রসেস ইনকমপ্লিট ও তার নিড কম বা সমান থাকে
                Finish[i] = True  # তাইলে প্রসেস কমপ্লিট হবে
                Work = np.add(Work, Allocation[i])  # তার ব্যাবহার করা রিসোর্স রিলিজ করে দিবে
                process_done.append(i)  # প্রসেস সেফ সিকুইয়েন্স
                process_incomplete -= 1
                flag = False

        if flag:  # যদি একটা প্রসেস ও কমপ্লিট করা না যায় তাহলে ডেডলক
            print("Deadlock Detected")
            break


Available = np.array([0, 0, 0])
Allocation = np.array([
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
])
Max = np.array([
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
])

detection_algorithm(Allocation, Max, Available)
