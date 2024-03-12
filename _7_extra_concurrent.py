
import time
import concurrent.futures


def hard_fn(a):
    time.sleep(3)
    return a ** 3


def run_3_calls_normal():
    t0 = time.time()

    data = [5, 10, 15]
    for x in data:
        print(hard_fn(x))

    print("run_3_calls_normal:", time.time() - t0)


def run_3_calls_parallel():
    t0 = time.time()

    data = [5, 10, 15, 5, 30, 100]
    tasks = []

    thread_pool_executor = concurrent.futures.ThreadPoolExecutor(10)

    with thread_pool_executor:
        for x in data:
            task = thread_pool_executor.submit(hard_fn, x)
            tasks.append(task)
            print(type(task))
            print(task.running())

        print(dir(tasks[0]))

        for finished_task in concurrent.futures.as_completed(tasks):
            print(finished_task.result())

    print("run_3_calls_parallel:", time.time() - t0)


if __name__ == '__main__':
    # run_3_calls_normal()
    run_3_calls_parallel()




# 125
# 1000
# 3375
# 9.001798868179321

# 125
# 1000
# 3375
# run_3_calls_parallel: 3.011631965637207