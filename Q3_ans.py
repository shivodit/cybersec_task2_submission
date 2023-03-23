Ct = "SYNT{Oehgrsbepr_vf_Rnfl}".upper()

for i in range(0,26):
    print(f"{i} \n")
    print("".join([(chr(65+((ord(x))+i)%26) if x.isalpha() else x) for x in Ct]))