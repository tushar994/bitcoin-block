from transaction_tracker import *
from read_input import *

tracker = Transaction_tracker(read_input())

# calling function that generates the block
ans = tracker.generate_block()

# function that gives the weight of the block
print("weight is ", tracker.tell_weight(ans))
# function that gives the fee of the block
print("fee is ", tracker.tell_fee(ans))


# writing the block into the txt file
f = open("block.txt", "w")

for element in ans:
    f.write(element + "\n")

