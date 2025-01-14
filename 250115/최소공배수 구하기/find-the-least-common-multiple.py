n, m = map(int, input().split())

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

lcm = n * m // gcd(n, m)

print(lcm)
