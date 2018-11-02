from KnotHash import *

list = list(range(256))
input_length = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]
k = KnotHash(list, input_length)
k.knot_list()
print(k.list[0] * k.list[1])
