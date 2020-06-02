import threading
import logging
import time

def fn_thread(val):
    l.acquire()
    logging.info("Thread %s: inizio", val)
    time.sleep(2)
    logging.info("Thread %s: fine", val)
    l.release()

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")
    logging.info("Padre: creo threads")

    threads = list()
    l = threading.Lock()

    for i in range(5):
        x = threading.Thread(target = fn_thread, args = (i, ))
        logging.info("Padre: creo e avvio thread %d", i)
        threads.append(x)
        x.start()
    
    for i,t in enumerate(threads):
        logging.info("Padre: prima dell'attesa del thread %d", i)
        t.join()
        logging.info("thread %d terminato", i)