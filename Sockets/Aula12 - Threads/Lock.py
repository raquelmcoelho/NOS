from threading import *
import time


def func(nome):
    for i in range(3):
        time.sleep(1)
        print(nome)


lock = Lock()
t = Thread(target=func, args=("raquel",))
t2 = Thread(target=func, args=("pedro",))
t.start()
lock.acquire()
t2.start()
print("Oi")
lock.release()


print("cabou tudo")