# psuedo-code, random in Java is nextInt, 1 LCG call
# nextInt(3) can only generate 0, 1, 2
import math
def mod(intNum, a):
    num = str(intNum)
    res = 0
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a;
    return res

def nextInt(bound, initial_seed):
    seed = mod(str((25214903917 * initial_seed) + 11), (2**48))
    if (bound == 0):
        out = int(seed)
        out << (48 - math.ceil(math.log(out, 2)))
        out = out >> 16
    elif (math.ceil(math.log(bound, 2)) == math.floor(math.log(bound, 2))):
        out = int(seed)
        out << (48 - math.ceil(math.log(out, 2)))
        out = out >> (48 - math.floor(math.log(bound, 2)))
    else:
        out = int(seed)
        out << (48 - math.ceil(math.log(out, 2)))
        out = out >> 17
        out = mod(out, bound)
    initial_seed = seed
    return out

def generate_cactus(seed_random, x, y, z):
    for l in range(0, 10):
        attempt_x = x + nextInt(8, initial_seed) - nextInt(8, initial_seed);
        attempt_y = y + nextInt(4, initial_seed) - nextInt(4, initial_seed);
        attempt_z = z + nextInt(8, initial_seed) - nextInt(8, initial_seed);
#        if (not air_block(attempt_x, attempt_y, attempt_z)) pass
        height = 1 + nextInt(nextInt(3, initial_seed) + 1, initial_seed)
#        for y_offset in range(0, height):
            # canBlockStay only valid with normal cactus conditions (on sand, no obstructions, etc.)
#            if (canBlockStay(attempt_x, attempt_y + y_offset, attempt_z))
#                setBlock(attempt_x, attempt_y + y_offset, attempt_z, Block.cactus)
        print("coord: " + str(attempt_x) + " " + str(attempt_y) + " " + str(attempt_z) + " --- height: " + str(height))



initial_seed = int(input("Cactus seed: "))
i = int(input("x chunk coord: "))
j = int(input("y chunk coord: "))
temp = 0

# i, j is seemingly chunk coord
k = 16*i
l = 16*j
# range(0, 1) is temp
for sth in range(0, 1):
    temp = nextInt(1, initial_seed)
    x = k + nextInt(16, initial_seed) + 8;
    temp = nextInt(1, initial_seed)
    y = nextInt(128, initial_seed);
    temp = nextInt(1, initial_seed)
    z = l + nextInt(16, initial_seed) + 8;
    new_cactus = generate_cactus(initial_seed, x, y, z)
