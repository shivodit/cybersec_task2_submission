with open("Q1.txt",'r') as f:
    lines = f.readlines()[:-4]

ans = ['']*63

for line in lines:
    for i ,j in enumerate(line):
        ans[i] = j if j != '.' else ans[i]

print("".join(ans)) 

# output kalmar{if_4t_first_you_d0nt_succeed_maybe_youre_us1ng_udp}