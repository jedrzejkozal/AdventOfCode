from KnotHash import *
from MultipleRounds import *
from copy import deepcopy

# numbers_list = list(range(256))
# input_length = [46, 41, 212, 83, 1, 255, 157, 65, 139, 52, 39, 254, 2, 86, 0, 204]
# k = KnotHash(numbers_list, input_length)
# k.knot_list()
# print("fist half", k.list[0] * k.list[1])
# assert k.list[0] * k.list[1] == 52070


new_input = "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204"
input_length = [ord(c) for c in new_input]
input_length.extend([17, 31, 73, 47, 23])

numbers_list = list(range(256))
k = KnotHash(numbers_list, input_length)

for _ in range(64):
    k.knot_list()

result_hash = ''
for i in range(0, len(k.list), 16):
    block = k.list[i:i+16]
    xor_result = block[0]
    for number in block[1:]:
        xor_result = xor_result ^ number
    xor_hex = hex(xor_result)[2:]
    if len(xor_hex) == 1:
        xor_hex = '0' + xor_hex
    print(xor_hex)
    result_hash += xor_hex

print(result_hash)
