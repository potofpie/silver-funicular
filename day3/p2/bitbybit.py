
from bitstring import BitArray



def read_file_to_array(filepath):
    with open(filepath) as f:
        return [l.strip() for l in f.readlines()]


def find_most_and_least_common_by_pos(lines):
    bit_count = [{'0':  0, '1':  0} for i in range(0,5)]
    for lindex, l in enumerate(lines):
        for cindex, c in enumerate(l.strip()):
            if(int(c) == 0 ):
                bit_count[cindex]['0'] = bit_count[cindex]['0']  + 1
            else:
                bit_count[cindex]['1'] = bit_count[cindex]['1']  + 1
    return bit_count



def agg_gamma_and_epsilon_rates(bit_count):
    epsilon = []
    gamma = []
    for bit_pos in bit_count:
        if bit_pos['0'] > bit_pos['1']:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
    return [epsilon, gamma]



if __name__ == "__main__":
    lines = read_file_to_array("../input.txt")
    bit_count = find_most_and_least_common_by_pos(lines)
    epsilon, gamma = agg_gamma_and_epsilon_rates(bit_count)











    epsilon = ''.join(epsilon)
    gamma = ''.join(gamma)
    print('\ngamma')
    print(gamma)
    print(f'int: {int(gamma, 2)} ')
    
    print('\nepsilon')
    print(epsilon)
    print(f'int: {int(epsilon, 2)} ')

    # print('\no2')
    # print(o2)
    # print(f'int: {int(o2, 2)} ')

    # print('\nco2')
    # print(co2)
    # print(f'int: {int(co2, 2)} ')
