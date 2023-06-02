import threading


def one(num):
    for i in range(num):
        print("A")


def two(num):
    for i in range(num):
        print("B")


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=one, args=(500,))
    t2 = threading.Thread(target=two, args=(500,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
