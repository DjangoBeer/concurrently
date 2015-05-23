import thread
import time

def fill(array, position):
    while True:
        array[position] += 1

array_to_fill = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(array_to_fill)):
    thread.start_new_thread(fill, (array_to_fill, i))

while True:
    print array_to_fill
    time.sleep(1)
