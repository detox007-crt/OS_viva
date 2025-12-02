import threading
import time
import random

# Shared Resources
data = 0
read_count = 0

# Locks
rc_lock = threading.Lock()   # Protects 'read_count'
wrt_lock = threading.Lock()  # Protects 'data' (Shared resource)

def reader(id):
    global read_count
    while True:
        # --- Entry Section ---
        with rc_lock:
            read_count += 1
            if read_count == 1:
                wrt_lock.acquire()  # First reader locks out writers

        # --- Critical Section ---
        print(f"Reader {id}: Reading data {data}")
        time.sleep(0.5)

        # --- Exit Section ---
        with rc_lock:
            read_count -= 1
            if read_count == 0:
                wrt_lock.release()  # Last reader releases writers
        
        time.sleep(random.random())

def writer(id):
    global data
    while True:
        # --- Entry & Critical Section ---
        with wrt_lock:
            data += 1
            print(f"Writer {id}: Writing data {data}")
            time.sleep(1)
            
        time.sleep(random.uniform(1, 2))

if __name__ == "__main__":
    # Start 5 Readers and 2 Writers
    for i in range(5): threading.Thread(target=reader, args=(i+1,)).start()
    for i in range(2): threading.Thread(target=writer, args=(i+1,)).start()
