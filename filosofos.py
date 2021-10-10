import random
import queue
import threading
import time

filosofoss = queue.Queue(maxsize=5)
nombres=[]
filosofosList=["a","b","c","d","e"]
#listanombres =5

def filosofoLista():
    

    for i in range (len(filosofosList)):
        a=0
        while a==0:
            #item = random.randint(1, listanombres)
            item = random.sample(filosofosList,1)
            if not item in nombres:
                nombres.append(item)
                a=1
        if not filosofoss.full():
            filosofoss.put(item)
        #print('Filosofo:',item,' ha empezado a comer')
        ##print("filosofos en cola:", filosofoss.qsize())
    


def filosofoServido():
    a=0
    while a<len(filosofosList):
        if not filosofoss.empty():
            item = filosofoss.get()
            print('Filosofo:',item,' ha empezado a comer')
            time.sleep(2)
            print('Filosofo:',item,'ha dejado de comer ')
            print("filosofos en cola:", filosofoss.qsize())
            print("\n")
            filosofoss.task_done()
            time.sleep(1)
            a=a+1

if __name__ == "__main__":

    threading_filosofoLista = threading.Thread(target=filosofoLista)
    threading_filosofoServido = threading.Thread(target=filosofoServido)

    threading_filosofoLista.start()
    threading_filosofoServido.start()
