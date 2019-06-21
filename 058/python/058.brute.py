def useful(x):
    if x < 32 or x > 122: return 0
    if x > 34 and x < 39: return 0
    if x == ord('/'): return 0
    if x == 64: return 0
    if x > 90 and x < 97: return 0
    return 1

# figure out values of a such that position (3*n) is useful
arange = range(97,123)
brange = range(97,123)
crange = range(97,123)
ranges = [arange, brange, crange]

for i in range(0, len(code)):
    rng = ranges[i % 3]
    c = code[i]
    j = 0
    while j < len(rng):
        if useful(c ^ rng[j]):
            j += 1
            continue
        rng.remove(rng[j])
        
print map(lambda x: chr(x), arange)
print map(lambda x: chr(x), brange)
print map(lambda x: chr(x), crange)