a = "Rex*cy*k*Hc~}cyo*Ezoxk~ced"

for i in range(1,501):
    if i ^ ord(a[0]) == ord('x'):
        print(i)
        print("".join([chr(ord(x)^i) for x in a ])) 

# alternate solution
# i = ord(a[0]) ^ ord("x")
