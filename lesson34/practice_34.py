import threading
import time
from concurrent.futures import ThreadPoolExecutor


def producer():
    print("set locker")
    # lock.acquire()
    # lock.acquire()
    with lock:
        print('acquired')
        with lock:
            print('acquired')
        print('released')
    print('released')

    # lock.release()


def producer_event():
    time.sleep(3)
    print("product is found!")
    
    prod_event.set()
    
    prod_event.clear()
    prod_event.set()
    prod_event.clear()


def consumer():
    print('waiting product')
    prod_event.wait()

    print('product exsists')


def producer_sem():
    with sem:
        print('semaph value', sem._value)
        time.sleep(3)
        print('free')


def exec_watcher():
    timer = threading.Timer(2, congrat)
    timer.start()


def congrat():
    print("Hello!")
    exec_watcher()



def long_process(start=0, finish=0):
    result = 0
    for _ in range(start, finish):
        result += 1
    return result


def run_executor(max_workers=4):
    executor = ThreadPoolExecutor(max_workers=max_workers)
    futures = []
    start_run = time.time()
    step = 2**24//max_workers
    for i in range(max_workers):
        future = executor.submit(long_process, i*step, (i+1)*step)
        futures.append(future)

    result = sum(future.result() for future in futures)
    print(result, time.time()-start_run)


def run_executor_map(max_workers=4):
    executor = ThreadPoolExecutor(max_workers=max_workers)
    futures = []
    start_run = time.time()
    step = 2**24//max_workers
    params = [[i*step, (i+1)*step] for i in range(max_workers)]
    # print(params)
    # futures = executor.map(long_process, *params)
    # print(futures)
    # result = sum(futures)
    result = sum(executor.map(long_process, *params))
    print(result, time.time()-start_run)


if __name__ == '__main__':
    lock = threading.Lock()
    # with
    # __enter__  .acquire()
    # __exit__   .release()
    #
    # 1. part
    # lock = threading.RLock()

    # task1 = threading.Thread(target=producer)
    # task2 = threading.Thread(target=producer)

    # task1.start()
    # task2.start()

    # task1.join()
    # task2.join()

    # 2. part
    prod_event = threading.Event()
    # task1 = threading.Thread(target=producer_event)
    # task2 = threading.Thread(target=consumer)
    # task3 = threading.Thread(target=consumer)

    # task1.start()
    # task2.start()
    # task3.start()

    # task1.join()
    # task2.join()
    # task3.join()

    # 3. part
    max_workers = 3
    sem = threading.Semaphore(value=max_workers)
    # sem = threading.BoundedSemaphore(value=max_workers)

    # tasks = []
    # task_count = 4

    # for i in range(task_count):
    #     task = threading.Thread(target=producer_sem)
    #     tasks.append(task)

    # for task in tasks:
    #     task.start()
    
    # sem.acquire()
    
    # for task in tasks:
    #     task.join()

    # sem.acquire()

    # 4. part
    # exec_watcher()

    # 5. part
    # run_executor()
    run_executor_map()



