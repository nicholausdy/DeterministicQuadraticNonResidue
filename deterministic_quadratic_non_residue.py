from math import log, floor
from fast_exponentiation import fast_pow

def find_quad_non_res_det(p):
    # p is a positive prime number
    # -999 means quadratic non-residue is not found
    # Use Extended Riemann Hypothesis to greatly reduce the total number of iterations (valid for p > 3)
    # Then use Euler's criterion to test whether the number is a quadratic non-residue or not
    result = -999
    i = 0
    if p != 2:
        if p == 3:
            result = 2
        else:
            a = 2
            max_iter = floor(3 * fast_pow(log(p), 2) / 2)
            while ((result == -999) and (a <= max_iter)):
                if ((fast_pow(a, ((p-1)/2)) % p) != 1):
                    result = a
                a = a + 1
                i = i + 1
    return result, i

p = 17
print(find_quad_non_res_det(p))

