def rshift(s, rpc, rt):
    rpc["FLAGS"] = "0" * 16
    s = s[6::]
    R_a = s[:3]
    imm_a = int(s[3:], 2)

    register = {
        "000": "R0",
        "001": "R1",
        "010": "R2",
        "011": "R3",
        "100": "R4",
        "101": "R5",
        "110": "R6",
    }
    R_a = register[R_a]

    rlist = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

    if R_a in rlist:
        temp = int(rpc[R_a], 2) >> imm_a
    else:
        print("N")

    temp = str(bin(temp))
    temp = temp[2::]

    x = len(temp)

    if x < 16:
        n = 16 - x
        temp = "0" * n + temp

    rpc[R_a] = temp
    rpc["PC"] = rpc["PC"] + 1

    return rpc, rt


# TEST

# rpc = {
#     "R0": "0000000000000000",
#     "R1": "0000000000101000",
#     "R2": "0000000010011000",
#     "R3": "0000000000000000",
#     "R4": "0000000000000000",
#     "R5": "0000000000000000",
#     "R6": "0000000000000000",
#     "FLAGS": "0000000000000000",
#     "PC": 10,
# }

# rpc = rshift("0100000100000010", rpc)

# for key, value in rpc.items():
#     print(key, ":", value)

# OUTPUT:

# R0 : 0000000000000000
# R1 : 0000000000001010
# R2 : 0000000010011000
# R3 : 0000000000000000
# R4 : 0000000000000000
# R5 : 0000000000000000
# R6 : 0000000000000000
# FLAGS : 0000000000000000
# PC : 11
