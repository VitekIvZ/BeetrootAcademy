#task1lesson34.py


"""
    A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module. 
Make the class have two global variables, one called counter set to 0, and another called rounds set 
to 100.000. Now implement the run() method, let it include a simple for-loop that iterates through 
rounds (e.i. 100.000 times) and for each time increments the value of the counter by 
1. Create 2 instances of the thread and start them, then join them and check the result 
of the counter, it should be 200.000, right? Run it a couple of times and consider some different 
reasons why you get the answer that you get. 
"""


import threading

# Global variables
counter = 0
rounds = 100000
lock = threading.Lock()  # Create a lock

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with lock:  # Acquire the lock before modifying the counter
                counter += 1
                
                
def main():
    # Create 2 instances of the Counter thread
    thread1 = Counter()
    thread2 = Counter()

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    # Check the result of the counter
    print(f"Final counter value: {counter}")
    
if __name__ == "__main__":
    main()
