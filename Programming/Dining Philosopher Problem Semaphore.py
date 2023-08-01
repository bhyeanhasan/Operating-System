import threading
import random
import time

philosopher = 5
Chopstick = [False, False, False, False, False]


def wait(n):
    global Chopstick
    while Chopstick[n] == True:
        print("Waiting for chopstick ", n)
    Chopstick[n] = True


def signal(n):
    global Chopstick
    Chopstick[n] = False


def eating(x, n):
    wait(n)
    wait((n + 1) % 5)
    print("Eating ", n)
    time.sleep(0.01)
    signal(n)
    signal((n + 1) % 5)
    print("Thinking ", n)
    print(threading.current_thread().name)


for i in range(200):
    n = random.randint(0, 4)
    t = threading.Thread(target=eating, args=('x', n))
    t.start()

# Deadlock
# t1 = threading.Thread(target=eating, args=('ij', 1))
# t2 = threading.Thread(target=eating, args=('ij', 2))
# t3 = threading.Thread(target=eating, args=('ij', 3))
# t4 = threading.Thread(target=eating, args=('ij', 4))
# t5 = threading.Thread(target=eating, args=('ij', 0))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
