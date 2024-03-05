"""
Queues
    - FIFO
    - append, pop(0)
"""

my_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

my_queue = []

for i in range(len(my_list)):
    my_queue.append(my_list[i])
    print(my_queue)

for i in range(len(my_list)):
    my_queue.pop(0)
    print(my_queue)
