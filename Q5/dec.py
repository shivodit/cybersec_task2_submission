import string
import math 

# flag="<<<FIND OUT>>>"
ct="BQOSRU{Moo3_K3q_Bt0lhfk3}"
flag2="PILANI{}"

known = "PILANI"
ct_known = ct[0:6]

key = '' # Variable for concatenating the key letters

aslow = "abcdefghijklmnopqrstuvwxyz"
ashigh = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i, j in zip(known,ct_known):
    if i in ashigh:
        key += ashigh[(-ashigh.index(i)+ashigh.index(j))%26]
    else:
        pass
        # your code for concatenating lowercase

print(key) 

# key MIDSEM

ans = ""
# decoding
j = 0
for i in ct:
    if i.isalpha():
        print(key[j])
        if i in ashigh:
            ans += ashigh[(ashigh.index(i) - ashigh.index(key[j]))%26]
        else:
            ans += aslow[(aslow.index(i) - ashigh.index(key[j]))%26]
    else:
        ans += i 
        continue
    if j == 5:
        j = 0
    else:
        j += 1

print(ans)

# PILANI{Agl3_S3m_Ph0deng3}