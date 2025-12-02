import os
import multiprocessing
import time

# --- CHILD PROCESS FUNCTION ---
def child_task():
    print(f"\n🟢 Child Process (PID: {os.getpid()})")
    print("   Child: Opening file to write...")
    
    # Open the file again in the child process
    # O_RDWR: Read/Write, O_APPEND: Add to end
    fd_child = os.open("test_sys.txt", os.O_RDWR | os.O_CREAT)
    
    data = b"System Calls in Python (Written by Child)\n"
    
    # File Related: write()
    os.write(fd_child, data)
    print("   Child: Data written.")
    
    # File Related: close()
    os.close(fd_child)
    print("   Child: Exiting.")

# --- MAIN BLOCK (REQUIRED FOR WINDOWS) ---
if __name__ == "__main__":
    print(f"Parent Process (PID: {os.getpid()})")
    print("Before creating child process")

    # Create the child process using multiprocessing instead of fork
    p = multiprocessing.Process(target=child_task)
    p.start()

    # --- PARENT PROCESS ---
    # Process Related: join() is the Windows equivalent of wait()
    p.join()
    
    print(f"\n🔵 Parent Process")
    print("   Parent: Child finished. Reading file...")

    # Open file to read
    fd = os.open("test_sys.txt", os.O_RDWR)
    
    # File Related: read()
    content = os.read(fd, 100)
    print(f"   Parent: Read data -> {content.decode().strip()}")
    
    # File Related: close()
    os.close(fd)