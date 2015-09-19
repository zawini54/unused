"""IMPROVED VERSION OF RULER.PY

Find is much slower than combinations

Find_first, randomize dual_combos, threads

*Randomize dual_combos

It should search for a random pair, find their difference, and check if it is already there or not.
If it's already there, search again. When all of them are filled, then we break the loop.

Modify combinations algorithm to make sure of the differences while looping, rather than filtering
"""
import time
import itertools

def find(length, num_req_bef):
    nums = list(range(0, length+1))
    if not combinations(nums, num_req_bef):  # weak security here. If the user passes in an arbritary number for num_req_bef, there will be no protection
        return num_req_bef + 1
    else:
        return num_req_bef

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

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    # first you create a tuple of the original input which you can refer later with
    # the corresponding indices
    n = len(pool)
    # get the length of the tuple
    if r > n:
        return
    # if the length of the desired permutation is higher than the length of the tuple
    # it is not possible to create permutations so return without doing something

    indices = list(range(r))
    # create the first list of indices in normal order ( indices = [0,1,2,3,...,r])
    # up to the desired range r

    #yield tuple(pool[i] for i in indices)
    # return the first permutation which is a tuple of the input with the original
    # indices up to r tuple(tuple[0], tuple[1],....,tuple[r])

    while True:
        for i in reversed(range(r)):
            # i will go from r-1, r-2, r-3, ....,0

            if indices[i] != i + n - r:
                # if condition is true except for the case
                # that at the position i in the tuple the last possible
                # character appears then it is equal and proceed with the character
                # before which means that this character is replaced by the next
                # possible one

                # example: tuple='ABCDE' so n = 5, r=3 indices is [0,1,2] at start i=2
                # yield (A,B,C)
                # indices[i] is 2 and checks if 2 != 4 (2 +5-3) is true and break
                # increase indices[i]+1 and yield (A,B,D)
                # indices[i] is 3 and checks if 3 != 4 (2 +5-3) is true and break
                # increase indices[i]+1 and yield (A,B,E)
                # indices[i] is 4 and checks if 4 != 4 (2 +5-3) is false so next loop
                # iteration:  i = 1 indices[i] is 1 and checks if 4 != 3 (1 +5-3)
                # is true and break .... and so on

                break
        else:
            # when the forloop completely finished then all possible character
            # combinations are processed and the function ends
            return

        # start filter
        c = tuple(pool[i] for i in indices) # tuple from code
        num_diffs = 0
        if c[0] == 0 and c[-1] == iterable[-1]:
            diffs = []
            dual_combos = itertools.combinations(c, 2)
            for d in dual_combos:
                diffs.append(d[1] - d[0])
            for x in range(1, iterable[-1]):
                if x in diffs:
                    num_diffs += 1

            if(num_diffs == iterable[-2]):
                return c

        indices[i] += 1 # as written proceed with the next character which means the
        # index at i is increased
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1 # all the following indexes are increased as
            # well since we only want to at following
            # characters and not at previous one or the
            # same which is index at indice[i]
