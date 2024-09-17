import threading

def list_numbers(thread_name):
    for i in range(1, 11):
        print(f"{thread_name}: {i}")

# Create a list to hold the thread objects
threads = []

# Create and start multiple threads
for i in range(5):  # Creating 5 threads as an example
    thread_name = f"Thread-{i+1}"
    thread = threading.Thread(target=list_numbers, args=(thread_name,))
    threads.append(thread)


for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished executing.")
