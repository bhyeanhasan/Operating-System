import threading

critical_section_available = True  # প্রথমে ক্রিটিকাল সেকশনে কেউ নেই


def release():
    global critical_section_available
    critical_section_available = True


def lock_critical():
    global critical_section_available

    while critical_section_available == False:
        print('\nAnother thread is using critical section\n')

    critical_section_available = False

    for i in range(100):
        print("\nusing ", threading.current_thread().name, "\n")

    release()


t1 = threading.Thread(target=lock_critical)
t2 = threading.Thread(target=lock_critical)

t1.start()
t2.start()
