import threading
import time

def count():
    for i in range(1, 6):
        print("Count:", i)
        time.sleep(1)

def square():
    for i in range(1, 6):
        print("Square:", i * i)
        time.sleep(1)

def cube():
    for i in range(1, 6):
        print("Cube:", i * i * i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=count)
    t2 = threading.Thread(target=square)
    t3 = threading.Thread(target=cube)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed.")

main()