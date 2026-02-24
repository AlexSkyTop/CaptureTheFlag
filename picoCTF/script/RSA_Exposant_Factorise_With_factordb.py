from Crypto.Util.number import *
from factordb.factordb import FactorDB

c = # Enter ciphertext here
n = # Enter modulus here
e = # Enter exposant here

f = FactorDB(n)
f.connect()
r = f.get_factor_list()
if len(r) >= 2 : print("Found :", r)
p = int(r[0])
q = int(r[1])
phi = (p-1)*(q-1)
d = inverse(e, phi)
decoded = long_to_bytes(pow(c, d, n))

print("DECODED : ", decoded)