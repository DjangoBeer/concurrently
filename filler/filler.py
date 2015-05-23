def fill(array, position):
    array[position] += 1

array_to_fill = [0, 0, 0, 0, 0, 0, 0, 0]

while True:
    for i in range(len(array_to_fill)):
        fill(array_to_fill, i)
        print array_to_fill