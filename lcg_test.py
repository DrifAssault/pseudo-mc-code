import math
def mod(num, a):
    res = 0
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a;
    return res
bound = None
initial_seed = 123123123
seed = mod(str((25214903917 * initial_seed) + 11), (2**48))
if (bound == None):
    out = int(seed)
    out << (48 - math.ceil(math.log(out, 2)))
    out = out >> 16
elif (math.ceil(math.log(bound, 2)) == math.floor(math.log(bound, 2))):
    out = int(seed)
    out << (48 - math.ceil(math.log(out, 2)))
    out = out >> (48 - math.floor(math.log(bound, 2)))
print(out)
