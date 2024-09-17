import threading


lock_a = threading.Lock()
lock_b = threading.Lock()
lock_c = threading.Lock()

def access_ab(thread_name):
    for i in range(1, 20):
        with lock_a:
            print(f"Acquired A from {thread_name}")
            block_bc(lambda: print(f"{thread_name}: processing from lock A and B and C ${i}"))

def block_bc(func):
    with lock_b:
        print(f"Acquired B from {thread_name}")
        with lock_c:
            print(f"Acquired C from {thread_name}")
            func()

def access_bc(thread_name):
    for i in range(1, 20):
        block_bc(lambda: print(f"{thread_name}: processing from lock C and B ${i}"))


# Create a list to hold the thread objects
threads = []

# Create and start multiple threads
for i in range(5):  # Creating 5 threads as an example
    thread_name = f"Thread- ABC - {i+1}"
    thread = threading.Thread(target=access_ab, args=(thread_name,))
    threads.append(thread)

for i in range(5):  # Creating 5 threads as an example
    thread_name = f"Thread- BC - {i+1}"
    thread = threading.Thread(target=access_bc, args=(thread_name,))
    threads.append(thread)

try:
    lock_a.acquire()
    print()
finally:
    lock_a.release()

for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished executing.")
