# psuedo-code, random in Java is nextInt, 1 LCG call
# random(3) can only generate 0, 1, 2
cactus_seed = int(input("Cactus seed: "))
# i, j is seemingly generated via
k = 16*i
l = 16*j
for sth in range(0, ):
    x = k + cactus_seed.random(16) + 8;
    y = cactus_seed.random(128);
    z = l + cactus_seed.random(16) + 8;
    new_cactus = generate_cactus(cactus_seed, x, y, z)

def generate_cactus(seed_random, x, y, z):
    for l in range(0, 10):
        attempt_x = x + random(8) - random(8);
        attempt_y = y + random(4) - random(4);
        attempt_z = z + random(8) - random(8);
        if (not air_block(attempt_x, attempt_y, attempt_z)) pass
        height = 1 + random(random(3) + 1)
        for y_offset in range(0, height):
            # canBlockStay only valid with normal cactus conditions (on sand, no obstructions, etc.)
            if (canBlockStay(attempt_x, attempt_y + y_offset, attempt_z))
                setBlock(attempt_x, attempt_y + y_offset, attempt_z, Block.cactus)
