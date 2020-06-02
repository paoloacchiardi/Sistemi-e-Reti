import time
import logging 
import threading

MAX = 10

def ping():
    i = 0
    while(i<MAX):
        i += 1
        s1.acquire()
        logging.info("ping")
        time.sleep(1)
        s2.release()

def pong():
    i = 0
    while(i<MAX):
        i += 1
        s2.acquire()
        logging.info("pong")
        time.sleep(1)
        s1.release()

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")

    t1 = threading.Thread(target = ping)
    t2 = threading.Thread(target = pong)
    s1 = threading.Lock()
    s2 = threading.Lock()
    s2.acquire()

    t1.start()
    t2.start()

    t1.join()
    t2.join()