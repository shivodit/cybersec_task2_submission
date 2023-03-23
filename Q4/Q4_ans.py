from factordb.factordb import FactorDB
import math

def calculate_private_key(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    return d,phi_n

ct = 8925700648516910493
# Example usage
n = 19473790491178967371 
f = FactorDB(n)
f.connect()
f = f.get_factor_list()

print(f)
p,q = f
e = 17
d , phi = calculate_private_key(p, q, e)
print(d) # Output: 413
print(pow(ct,d,n))
