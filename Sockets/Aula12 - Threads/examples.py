import threading
import time
import datetime
import logging


# def worker(message):
#     for i in range(1, 6, 1):
#         print(f"\n{datetime.datetime.now().second} : {datetime.datetime.now().microsecond} {message} {str(i)}")
#         time.sleep(1)
#
#
# t = threading.Thread(target=worker, args=(' Thread na execução',))
# t.start()
#
# tempo = 0
# while t.is_alive():
#     print(f'\n{datetime.datetime.now().second} : {datetime.datetime.now().microsecond} Aguardando thread')
#     time.sleep(1)
#     tempo += 1
#
# print('XXXX Thread morreu')
# print('0000 Finalizando programa')

#####################################################################################

# def thread_delay(thread_name, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         print('-------->', time.strftime(format("%H: %M :%S",)), thread_name)
#         count += 1
#     print("se passaram 5 vezes o tempo na thread ", thread_name)
#     t2.start()
#
#
# t1 = threading.Thread(target=thread_delay, args=('0000', 2))
# # 5
# t2 = threading.Thread(target=thread_delay, args=('||||', 3))
# # 15
# t1.start()

########################################################################################

# def thread_function(name):
#     logging.info("Thread %s: iniciando", name)
#     time.sleep(2)
#     logging.info("Thread %s: finalizando", name)
#
#
# if __name__ == "__main__":
#     formato = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=formato, level=logging.INFO)
#     logging.info("Main : antes de criar thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main : antes de rodar thread")
#     x.start()
#     logging.info("Main : esperando pela thread finalizar")
#     x.join()
#     logging.info("Main : tudo pronto")

############################################################################


# def thread_function(name):
#     logging.info("Thread %s: iniciando", name)
#     time.sleep(2)
#     logging.info("Thread %s: finalizando", name)
#
#
# if __name__ == "__main__":
#     formato = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=formato, level=logging.INFO, datefmt="%H:%M:%S")
#
#     threads = list()
#     for index in range(3):
#         logging.info("Main : cria e inicializa thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()
#
#     for index, thread in enumerate(threads):
#         logging.info("Main : antes de sincronizar thread %d.", index)
#         thread.join()
#         logging.info("Main : thread %d pronta", index)

##########################################################################################
# import concurrent.futures
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     future1 = executor.submit(pow, 2, 3)
#     future2 = executor.submit(pow, 5, 8)
#     print(future1.result(), future2.result())

##########################################################################################

import math
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor()
future1 = executor.submit(pow, 2, 3)
result1 = future1.result()
future2 = executor.submit(math.sqrt, result1)
print(future2.result())