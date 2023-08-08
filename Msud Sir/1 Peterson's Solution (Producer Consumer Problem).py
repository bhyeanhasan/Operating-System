import threading

Critical_item = 0  # critical data
Producer_wish = False
Consumer_wish = False
turn = -1  # 0 mane Producer 1 mane Consumer


def producer_want_to_produce():
    global Critical_item, Producer_wish, Consumer_wish, turn
    Producer_wish = True
    turn = 1  # mane holo producer age consumer ke chance dibe

    while Consumer_wish == True and turn == 1:
        print('Producer is waiting and Consumer is in Critical section')

    # jodi upor er loop false hy, tar mane consumer ar use korbena , so Producer Critical Section e jete parbe
    Critical_item = Critical_item + 1
    for i in range(100):
        print("Producer critical section e ace")
    Producer_wish = False
    print('Producer critical section use kora ses')


def consumer_want_to_consume():
    global Critical_item, Producer_wish, Consumer_wish, turn
    Consumer_wish = True
    turn = 0  # mane holo Consumer age Producer ke chance dibe

    while Producer_wish == True and turn == 0:
        print('Consumer is waiting and Producer is in Critical section')

    # jodi upor er loop false hy, tar mane Producer ar use korbena , so Consumer Critical Section e jete parbe
    Critical_item = Critical_item - 1
    for i in range(100):
        print("Consumer critical section e ace")
    Consumer_wish = False
    print('Consumer critical section use kora ses')


t1 = threading.Thread(target=producer_want_to_produce)
t2 = threading.Thread(target=consumer_want_to_consume)

t1.start()
t2.start()
