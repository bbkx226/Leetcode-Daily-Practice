def qpow(a, b):
    ret = 1
    while b>0:
        if b & 1:
            ret *= a
        a *= a
        b >>= 1

    return ret

print(qpow(2, 3))

def qmult(a, b, mod):
    ret = 0
    while b > 0:
        if b & 1:
            ret = (ret + a) % mod
        a = (a + a) % mod
        b >>= 1
    return ret