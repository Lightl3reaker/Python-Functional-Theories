import time


def myfunc(fn, *args, rep=0, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    avgTime = (end-start)/rep
    fn(avgTime)


myfunc(print, 1, 2, 3, sep='-', end="****\n", rep=5)
