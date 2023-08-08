import threading
import random
import time

philosopher = 5
Chopstick = [False, False, False, False, False]  # একদম প্রথমে কেউ চপস্টিক হাতে নেয় নাই


def wait(n):  # চপস্টিক হাতে নিবে
    global Chopstick
    while Chopstick[n] == True:  # n তম চপস্টিক অলরেডি আরেকজন নিয়া নিছে, তাই ও অপেক্ষা করবে
        print("Waiting for chopstick ", n)

    Chopstick[n] = True


def signal(n):  # চপস্টিক রেখে দিবে
    global Chopstick
    Chopstick[n] = False


def eating(x, n):
    wait(n)  # তার বাম পাশের চপস্টিকের খালি থাকলে নিবে নইলে অপেক্ষা করবে
    wait((n + 1) % 5)  # তার ডান পাশের চপস্টিকের খালি থাকলে নিবে নইলে অপেক্ষা করবে

    print("\n Eating ", n, " \n")
    time.sleep(4)

    signal(n)  # বাম হাতের চপস্টিক রেখে দিবে
    signal((n + 1) % 5)  # ডান হাতের চপস্টিক রেখে দিল

    print("\n Thinking ", n, threading.current_thread().name, "\n")


# for i in range(4):
#     n = random.randint(0, 4)
#     t = threading.Thread(target=eating, args=('x', n))
#     t.start()

# সিমাফোর সলুশনে ডেড লক আসতে পারে, যখন ৫ জন লোকই একটা করে চপস্টিক হাতে নিয়ে আরেকটার জন্য অপেক্ষা করবে, আজীবন অপেক্ষা করা লাগবে

t1 = threading.Thread(target=eating, args=('ij', 1))
t2 = threading.Thread(target=eating, args=('ij', 2))
t3 = threading.Thread(target=eating, args=('ij', 3))
t4 = threading.Thread(target=eating, args=('ij', 4))
t5 = threading.Thread(target=eating, args=('ij', 0))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
