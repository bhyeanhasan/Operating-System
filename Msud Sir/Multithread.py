import threading


def one(num, char):
    for i in range(num):
        print(char)


# creating thread
t1 = threading.Thread(target=one, args=(100, 't1'))
t2 = threading.Thread(target=one, args=(50, 't2'))
t3 = threading.Thread(target=one, args=(100, 't3'))

t1.start()
t2.start()
t3.start()

t2.join()
print("T2 ses na houa porjonto wait koro")


