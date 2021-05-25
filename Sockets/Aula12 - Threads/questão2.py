"""
2. Fazer um script em Python que utilize múltiplas threads (5) em que cada thread
exibe a hora atual em sequência num intervalo determinado, porém as threads
são executadas em tempos aleatórios. Por exemplo, T1 5 segundos, T2 7
segundos, T3 13 segundos, T4 23 segundos e T5 26 segundos. A informação
exibida deve identificar também a Thread que está exibindo a informação.
Utilize prints ou logs para exibir as informações.
"""

import threading
import time
import logging
import random

logging.basicConfig(format=" %(asctime)s - %(message)s", level=logging.INFO)


def delay(idthread, tempo):
    logging.info(f"Execução da thread {idthread} que vai custar {tempo} segundos")
    time.sleep(tempo)
    logging.info(f"Finalização da thread {idthread}")


for i in range(5):
    t = threading.Thread(target=delay, args=(i, random.choice(range(30))))
    t.start()
