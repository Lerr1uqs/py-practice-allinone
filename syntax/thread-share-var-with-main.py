import time
import threading

class Counter:
    def __init__(self) -> None:
        self.number = 0
    
def worker(counter: Counter):
    for i in range(5):
        time.sleep(0.5)
        print(f"{counter.number}")

def writer(counter: Counter):
    for i in range(5):
        time.sleep(0.5)
        counter.number += 1


counter = Counter()
t1 = threading.Thread(target=worker, args=(counter, ))

t1.start()
writer(counter)

t1.join()
'''
0
2
2
3
5
'''