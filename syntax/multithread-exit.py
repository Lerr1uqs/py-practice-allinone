import time
import threading

def worker():
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        import sys
        sys.exit(0)

def boss():
    for i in range(5):
        time.sleep(1)
        print(i)


t1 = threading.Thread(target=worker, args=())
t2 = threading.Thread(target=boss, args=())

t1.start()
t2.start()

t1.join()
t2.join()

# 一个线程从exit退出不会影响另外的线程 会有锁报错
'''
0
^CTraceback (most recent call last):
  File "syntax/multithread-exit.py", line 23, in <module>
    t1.join()
  File "/usr/lib/python3.8/threading.py", line 1011, in join
    self._wait_for_tstate_lock()
  File "/usr/lib/python3.8/threading.py", line 1027, in _wait_for_tstate_lock
    elif lock.acquire(block, timeout):
KeyboardInterrupt
1
2
3
4

'''