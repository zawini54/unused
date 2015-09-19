from ruler import *

range_bot = 1  #prompt_int("MinRange: ")
range_top = prompt_int("MaxRange: ") + 1
# amount_processes = prompt_int("Amount of processes to run: ")
start = time.time()
num_req_bef_loop = 1
if range_bot == 0:
    range_bot = 1
for x in range(range_bot, range_top):
    num_req_bef_loop = find(x, num_req_bef_loop)
    print(x, int(num_req_bef_loop))

print("Completed in ", time.time() - start, "seconds")
