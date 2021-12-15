
from bitstring import BitArray


bit_count = [{'0':  0, '1':  0} for i in range(0,12)]

with open('../input.txt') as f:
    lines = f.readlines()
    for lindex, l in enumerate(lines):
        for cindex, c in enumerate(l.strip()):
            if(int(c) == 0 ):
                bit_count[cindex]['0'] = bit_count[cindex]['0']  + 1
            else:
                bit_count[cindex]['1'] = bit_count[cindex]['1']  + 1

epsilon = []
gamma = []

for bit_pos in bit_count:
    if bit_pos['0'] > bit_pos['1']:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

epsilon = ''.join(epsilon)
gamma = ''.join(gamma)

print('gamma')
print(gamma)
print(f'int: {int(gamma, 2)} ')
print('epsilon')
print(epsilon)
print(f'int: {int(epsilon, 2)} ')
