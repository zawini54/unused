"""THE ORIGINAL EDITION OF RULE.PY"""

import time
from multiprocessing import Pool
import itertools

def find(length):
    list = []
    indices = length+1
    num_combos = 0
    for n in range(0, length+1):
        list.append(n)
    tf = []
    while indices >= 2:
        combos = itertools.combinations(list, indices)
        for c in combos:
            num_combos += 1
            contains_all_diffs = True
            if c[0] == 0 and c[indices-1] == length:
                diffs = []
                dual_combos = itertools.combinations(c, 2)
                for d in dual_combos:
                    diffs.append(d[1] - d[0])
                for x in range(1, length+1):
                    if not(x in diffs):
                        contains_all_diffs = False
                tf.append((contains_all_diffs, c))
        indices -= 1
    num_req = length+1
    for a in tf:
        if a[0]:
            num_req = len(a[1])
    return (num_req, num_combos)  #added num_combos

def prompt_int(string):
    isNum = False
    while not isNum:
        num = input(string)
        try:
            num = int(num)
            isNum = True
            return num
        except:
            print("Not an integer")
            isNum = False

#init
length = prompt_int("Length of ruler: ")
amount_processes = prompt_int("Amount of processes to run: ")
start = time.time()
total_amount_combos = 0  #related to num_combos
with Pool(amount_processes) as p:
    vals = p.map(find, range(1, length+1))
for x in range(1, length+1):
    total_amount_combos += vals[x-1][1]
    print(x, ",", vals[x-1][0])

print("\n"+str(total_amount_combos), "total amount of combos run in", time.time() - start, "seconds")
