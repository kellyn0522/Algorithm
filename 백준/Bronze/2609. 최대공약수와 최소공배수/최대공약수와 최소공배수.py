import math

a, b = map(int, input().split())

gcd_max = math.gcd(a, b)
lcm_min = math.lcm(a, b)

print(gcd_max)
print(lcm_min)