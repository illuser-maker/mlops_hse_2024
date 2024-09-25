import time
import threading
import multiprocessing
import requests
import concurrent.futures

def cpu_bound(number):
    return sum(i * i for i in range(number))

def io_bound(url):
    return requests.get(url).text[:100]

def run_tasks_in_parallel(func, tasks, num_workers, use_threads=True):
    if use_threads:
        executor_class = concurrent.futures.ThreadPoolExecutor
    else:
        executor_class = concurrent.futures.ProcessPoolExecutor

    with executor_class(max_workers=num_workers) as executor:
        results = list(executor.map(func, tasks))
    return results

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return end - start

def compare_parallel_methods(task_type, num_tasks, num_workers):
    if task_type == "cpu":
        numbers = [10**7 + x for x in range(num_tasks)]

        thread_time = measure_time(run_tasks_in_parallel, cpu_bound, numbers, num_workers, True)
        process_time = measure_time(run_tasks_in_parallel, cpu_bound, numbers, num_workers, False)

        print(f"CPU-bound task:")
        print(f"Threading time: {thread_time:.2f} seconds")
        print(f"Multiprocessing time: {process_time:.2f} seconds")

    elif task_type == "io":
        urls = ["http://example.com" for _ in range(num_tasks)]

        thread_time = measure_time(run_tasks_in_parallel, io_bound, urls, num_workers, True)
        process_time = measure_time(run_tasks_in_parallel, io_bound, urls, num_workers, False)

        print(f"I/O-bound task:")
        print(f"Threading time: {thread_time:.2f} seconds")
        print(f"Multiprocessing time: {process_time:.2f} seconds")

if __name__ == "__main__":
    num_tasks = 10
    num_workers = 4

    print("Comparing parallel methods for CPU-bound tasks:")
    compare_parallel_methods("cpu", num_tasks, num_workers)
    num_tasks = 50
    print("\nComparing parallel methods for I/O-bound tasks:")
    compare_parallel_methods("io", num_tasks, num_workers)