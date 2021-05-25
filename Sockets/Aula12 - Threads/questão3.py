"""
3. Criar um script em que threads cooperam para determinar se um conjunto de
cinco números (estáticos) disponibilizados em uma lista são primos ou não. Cada
thread deve ser responsável por um número e exibir uma mensagem informando
o resultado
"""
import logging
import threading
import concurrent.futures

primosduvida = [0, 3, 4, 7, 11]
executor = concurrent.futures.ThreadPoolExecutor()
logging.basicConfig(format='%(asctime)s ---- %(message)s', level=logging.INFO)


def checar_primo(idt, num):
    # primos só são divisíveis por 1 e por eles mesmos, logo são excluídos do range
    for i in range(2, num):
        if num % i == 0:
            logging.info(f"A thread {idt} reconheceu que o número {num} não é primo")
            return False
    logging.info(f"A thread {idt} reconheceu que o número {num} é primo")
    return True


for idthread, numero in enumerate(primosduvida):
    x = threading.Thread(target=checar_primo, args=(idthread, numero))
    x.start()
