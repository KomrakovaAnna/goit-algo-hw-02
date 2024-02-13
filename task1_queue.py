from queue import Queue
import random

queue = Queue()

def generate_request():
    new_request = random.randint(1, 5)
    queue.put(new_request)
    print(f"New request has been generated {new_request} added to the queue")

def process_request():
    if queue.empty():
        print("Queue is empty")
    else:
        request = queue.get()
        print(f"Processed: {request}")

while True:
    choice = input("Print generate to generate request, process to process requst, stop to quit >>> ").lower()
    if choice == "generate":
        generate_request()
    elif choice == "process":
        process_request()
    elif choice == "stop":
        print("Bye!")
        break
    else:
        print("Incorrect input. Try again. Print generate to generate request, process to process requst, stop to quit")
