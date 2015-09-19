import random
import itertools
def rand_dual_combos(iterable):
    diffs_got = []
    while len(diffs_got) <= iterable[-2]:
        num_bot = random.randint(0, iterable[-1]) # dangerous
        num_top = random.randint(0, iterable[-1])
        if num_bot == num_top:
            continue
        elif num_bot > num_top:
            if (num_bot - num_top) in diffs_got:
                continue
            else:
                diffs_got.append(num_bot - num_top)
        elif num_bot > num_top:
            if (num_bot - num_top) in diffs_got:
                continue
            else:
                diffs_got.append(num_bot - num_top)

    print(diffs_got)
def combinations_with_explanation(iterable, r):
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

            if num_diffs == iterable[-2]:
                return c

        indices[i] += 1 # as written proceed with the next character which means the
        # index at i is increased
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1 # all the following indexes are increased as
            # well since we only want to at following
            # characters and not at previous one or the
            # same which is index at indice[i]


# TBD
def combos_dual(ls):
    diffs = []
    pool = tuple(ls)
    n = len(pool)

    if 2 > n:
        return

    indices = list(range(2))

    c = tuple(pool[i] for i in indices)
    diffs.append(c[1] - c[0])

    while True:
        for i in reversed(range(2)):
            if indices[i] != i + n - 2:
                break
        else:
            return

        indices[i] += 1
        for j in range(i+1, 2):
            indices[j] = indices[j-1] + 1

        c = tuple(pool[i] for i in indices)
        if c[0] > c[1]:
            diff = c[0] - c[1]
        elif c[1] > c[0]:
            diff = c[1] - c[0]

        if not diff in diffs:
            diffs.append(diff)
        elif len(diffs) == ls[-1]:
            break
    return c