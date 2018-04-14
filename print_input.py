#!/usr/bin/python

import multiprocessing as mp

# define the work of each process as a function
def print_input(input):
    print(input)

# create an empty array
processes = []

num_procs = 4

# create all the processes
for i in range(num_procs):
    processes.append(mp.Process(target=print_input, args=([i])))

# begin each process
for p in processes:
    p.start()

# here we should see each input printed out, not necessarily in order

# end each process
for p in processes:
    p.join()

