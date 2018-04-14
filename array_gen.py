#!/usr/bin/python

import multiprocessing as mp

# create a lock object so that the counter can be incremented and the array can be accessed atomically
array_lock = mp.Lock()

# choose number of processes
num_procs = 4

mpVals = mp.Array('i', num_procs+1, lock=False)
mpVals[num_procs] = 0

# define  work that each process does atomically
def mp_array(input, array):
    with array_lock:
        mpVals[mpVals[num_procs]] = input
        mpVals[num_procs] += 1
        
# create an empty processes array
processes = []

# create all the processes
for i in range(num_procs):
    processes.append(mp.Process(target=mp_array, args=([i, mpVals])))

# begin each process
for p in processes:
    p.start()

# here we should see each input printed out, not necessarily in order

# end each process
for p in processes:
    p.join()

for i in mpVals:
    print(i)

