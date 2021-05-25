"""1. Escrever um script “hello, world” multi-threaded. Cada thread deve exibir a
mensagem padrão com uma personalização (id da thread, parâmetro passado
na criação, data/hora, etc).ser responsável por um número e exibir uma mensagem informando
o resultado"""

import threading
import logging

formato = "%(asctime)s -  %(message)s"
logging.basicConfig(format=formato, level=logging.INFO, datefmt="%H: %M: %S")


def criar(num):
    logging.info(f"Eu sou a thread número {num}")


for i in range(7):
    t = threading.Thread(target=criar, args=(i,))
    t.start()
