
from bitstring import BitArray


BYTE_SIZE = 12


def read_file_to_array(filepath):
    with open(filepath) as f:
        return [l.strip() for l in f.readlines()]


def find_most_and_least_common_by_pos(lines):
    bit_count = [{'0':  0, '1':  0} for i in range(0,BYTE_SIZE)]
    for lindex, l in enumerate(lines):
        for cindex, c in enumerate(l.strip()):
            if(int(c) == 0 ):
                bit_count[cindex]['0'] = bit_count[cindex]['0']  + 1
            else:
                bit_count[cindex]['1'] = bit_count[cindex]['1']  + 1
    return bit_count



def get_o2_rate(lines, index):
    temp = []
    bit_count = find_most_and_least_common_by_pos(lines)
    for i in lines:
        # print(i, index)
        if (bit_count[index]['1'] > bit_count[index]['0']) and i[index] == '1':
            temp.append(i)
        elif (bit_count[index]['1'] < bit_count[index]['0']) and i[index] == '0':
            temp.append(i)
        elif   (bit_count[index]['1'] == bit_count[index]['0']) and i[index] == '1':
            temp.append(i)
    if(len(temp) == 1):
        return temp[0]
    else:
        # print(temp)
        return get_o2_rate(temp,index+1 )


def get_co2_rate(lines, index):
    temp = []
    bit_count = find_most_and_least_common_by_pos(lines)
    for i in lines:
        if (bit_count[index]['1'] > bit_count[index]['0']) and i[index] == '0':
            # print(i)
            temp.append(i)
        elif (bit_count[index]['1'] < bit_count[index]['0']) and i[index] == '1':
            # print(i)
            temp.append(i)
        elif (bit_count[index]['1'] == bit_count[index]['0']) and i[index] == '0':
            # print(i)
            temp.append(i)
    if(len(temp) == 1):
        return temp[0]
    else:
        # print(temp)
        return get_co2_rate(temp,index+1 )




if __name__ == "__main__":
    lines = read_file_to_array("../input.txt")
    print()
    print()

    print(f'o2: {int(get_o2_rate(lines, 0), 2)}')
    print(f'co2: {int(get_co2_rate(lines, 0), 2)}')


