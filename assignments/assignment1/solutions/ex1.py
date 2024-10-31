def gcd(a, b):
    while not a == b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

ax = 42
bx = 30
print("GCD of", ax, "and", bx, "is", gcd(ax, bx))

def test_euclid():
    ax = 42
    bx = 30
    r = gcd(ax, bx)
    assert r == 6