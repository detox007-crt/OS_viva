import threading
import time
import random

# Buffer (Shared Resource)
buffer = []
BUFFER_SIZE = 5   # Max capacity of buffer

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Controls empty slots
full = threading.Semaphore(0)             # Controls filled slots
mutex = threading.Lock()                  # Mutex lock for critical section

def producer():
    while True:
        item = random.randint(1, 100)  # Producing random item
        empty.acquire()  # Wait if buffer is full
        
        mutex.acquire()  # Enter critical section
        buffer.append(item)
        print(f"🟢 Producer produced: {item} | Buffer: {buffer}")
        mutex.release()  # Exit critical section
        
        full.release()   # Signal that buffer has new item
        time.sleep(random.uniform(0.5, 1.5))

def consumer():
    while True:
        full.acquire()  # Wait if buffer is empty
        
        mutex.acquire()  # Enter critical section
        item = buffer.pop(0)
        print(f"🔴 Consumer consumed: {item} | Buffer: {buffer}")
        mutex.release()  # Exit critical section
        
        empty.release()  # Signal that buffer has space
        time.sleep(random.uniform(0.5, 1.5))


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
