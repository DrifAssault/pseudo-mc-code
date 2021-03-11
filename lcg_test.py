bound = int(input("test? "))
seed = (25214903917 * seed + 11) % (2**48)
if (bound == None) {return seed >> 16}
elif (math.ceil(Log2(bound)) == math.floor(Log2(bound))){
    return seed >> (31 - math.floor(Log2(bound)))}
