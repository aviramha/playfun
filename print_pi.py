"""Print pi to many decimal places using the mpmath library."""

from mpmath import mp, pi

# Set precision to 100 decimal places
mp.dps = 100

print(f"π = {pi}")
