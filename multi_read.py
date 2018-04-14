#!/usr/bin/python

import multiprocessing as mp
import numpy as np

# choose number of processes
num_procs = 4

num_things_per_proc = 10

# create a list of things from which to operate
mpVals = mp.Array('i', num_procs*num_things_per_proc, lock=False)

# populate the array in serial, cause this is cheap
for i in range(num_procs*num_things_per_proc):
    mpVals[i] = i

# create a lock object for atomicity
array_lock = mp.Lock()

# define work that each process does atomically
def print_segment(id, segment_start_index, segment_end_index):
    #with array_lock:
        for i in range(segment_start_index, segment_end_index):
            print ("Process: " + str(id) + ", value: " + str(mpVals[i]))

# create an empty processes array
processes = []

# create all the processes
for i in range(num_procs):
    processes.append(mp.Process(target=print_segment, args=([i, i*num_things_per_proc, (i+1)*num_things_per_proc])))

# begin each process
for p in processes:
    p.start()

# here we should see each input printed out, not necessarily in order

# end each process
for p in processes:
    p.join()

#for i in range(num_procs):
#    print(i)

