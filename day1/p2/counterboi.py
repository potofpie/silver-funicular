
def window_sum(array, index, window_size):
    try:
        window_sum = 0
        for i in range(0, window_size):
            window_sum = window_sum + array[index+i]
        return window_sum
    except:
        return 0



c=0
with open('../input.txt') as f:
    lines = f.readlines()
    # print(len(lines))
    readings = [int(i.strip()) for i in lines]
    # print(readings)

    for lindex, l in enumerate(lines):
        if(lindex != 0):
            if window_sum(readings, lindex-1, 3) < window_sum(readings, lindex, 3):
                c+=1
print(c)