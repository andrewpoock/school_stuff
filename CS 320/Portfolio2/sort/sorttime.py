# sorttime.py
#  useful functions for sorting experiments

import random
import time


def test_sort(sortfn, size, inplace=True):
    """test sortfn on random list of given size

    """
    old = [random.random() for _ in range(size)]
    if inplace:
        new = list(old)
        sortfn(new)
    else:
        new = sortfn(old)
    assert set(old) == set(new), "Elements not the same"
    assert all(new[i] <= new[i+1] for i in range(size-1)), "Not ordered"
    print("Test Successful")


def time_sort(fn, size, order="random"):
    """ time sorting function fn on list of a given size

    """
    assert order in ["random", "increasing", "decreasing"]
    lst = [random.random() for _ in range(size)]
    if order != "random":
        lst.sort()
    if order == "decreasing":
        lst.reverse()
    start = time.time()
    fn(lst)
    end = time.time()
    return end-start


def run_sort_trials(sortfn, list_sizes, trials, order="random"):
    """Run sort timing trials
    e.g. run_sort_trials(ins_sort, [1000, 5000, 10000], 5)

    """
    print("Running Trials")
    print(f"Start Trials: {sortfn.__name__}")
    print(f"Sizes: {list_sizes}")
    print(f"Num Trials: {trials}")
    averages = []
    for list_size in list_sizes:
        print(f"\nCurrent Size: {list_size}")
        times = []
        for trial in range(1, trials+1):
            timing = time_sort(sortfn, list_size, order)
            times.append(timing)
            print(f"    trial {trial}: {timing:0.5f}")
        average = sum(times)/trials
        print("    ----------------")
        print(f"    Average: {average:0.5f}")
        averages.append((list_size, average))
    print(f"\nEnd Trials: {sortfn.__name__}")
    return averages
