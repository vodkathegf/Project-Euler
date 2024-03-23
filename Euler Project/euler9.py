# the pythagorean triplet for which a + b + c = 1000
# find abc product

def pythagorean_triplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, (target_sum - a) // 2):
            c = target_sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
    return None


target_sum = 1000

triplet = pythagorean_triplet(target_sum)

if triplet:
    a, b, c = triplet
    product = a * b * c
    print(
        f" pythagorean is satisfied with only one triplet a = {a} b = {b} c = {c} product = {product}")
