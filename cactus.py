# psuedo-code, random in Java is nextInt, 1 LCG call
# nextInt(3) can only generate 0, 1, 2
import math
def mod(num, a):
    res = 0
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a;
    return res

seed = int(input("Cactus seed: "))
bound = int(input("Bound (if you wanna have no bound, put 0): "))
i = int(input("x chunk coord?"))
j = int(input("y chunk coord?"))

def nextInt(bound):
    seed = mod(str((25214903917 * seed) + 11), (2**48))
    if (bound == 0):
        out = int(seed)
        out << (48 - math.ceil(math.log(out, 2)))
        out = out >> 16
    elif (math.ceil(math.log(bound, 2)) == math.floor(math.log(bound, 2))):
        out = int(seed)
        out << (48 - math.ceil(math.log(out, 2)))
        out = out >> (48 - math.floor(math.log(bound, 2)))
    return out

# i, j is seemingly chunk coord
k = 16*i
l = 16*j
for sth in range(0, ?):
    x = k + seed.nextInt(16) + 8;
    y = seed.nextInt(128);
    z = l + seed.nextInt(16) + 8;
    new_cactus = generate_cactus(seed, x, y, z)

def generate_cactus(seed_random, x, y, z):
    for l in range(0, 10):
        attempt_x = x + nextInt(8) - nextInt(8);
        attempt_y = y + nextInt(4) - nextInt(4);
        attempt_z = z + nextInt(8) - nextInt(8);
        if (not air_block(attempt_x, attempt_y, attempt_z)) pass
        height = 1 + nextInt(nextInt(3) + 1)
        for y_offset in range(0, height):
            # canBlockStay only valid with normal cactus conditions (on sand, no obstructions, etc.)
            if (canBlockStay(attempt_x, attempt_y + y_offset, attempt_z))
                setBlock(attempt_x, attempt_y + y_offset, attempt_z, Block.cactus)
