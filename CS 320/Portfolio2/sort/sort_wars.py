# sort_wars.py
# Sort Wars script
# Andrew Poock

from sorttime import *
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort, insertion_sort2
from selection_sort import selection_sort
from shell_sort import shell_sort

def main():
    run_sort_trials(bubble_sort, [1000, 5000, 10000], 5)
    run_sort_trials(insertion_sort, [1000, 5000, 10000], 5)
    run_sort_trials(insertion_sort2, [1000, 5000, 10000], 5)
    run_sort_trials(selection_sort, [1000, 5000, 10000], 5)
    run_sort_trials(shell_sort, [1000, 5000, 10000], 5)


main()