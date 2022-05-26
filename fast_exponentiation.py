def fast_pow(base, pow):
# Compute base^pow using binary method for fast computation
# Requirements:
# pow >= 0
    result = 1
    while (pow > 0):
        if (pow % 2 != 0):
            result = result * base
        base = base * base
        pow = pow // 2
    return result

# print(fast_pow(8,6))
