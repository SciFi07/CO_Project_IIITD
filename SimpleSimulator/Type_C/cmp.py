def cmp(s, rpc, rt):

    rpc["FLAGS"] = "0" * 16
    flag = "0" * 12
    s = s[10::]
    R_a = s[:3]
    R_b = s[3:6]

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
    R_b = register[R_b]
    if rt[R_a] == 'float':
        return "ERROR:REGISTER WITH FLOAT VALUE"
    if rt[R_b] == 'float':
        return "ERROR:REGISTER WITH FLOAT VALUE"
    R_a = int(rpc[R_a], 2)
    R_b = int(rpc[R_b], 2)

    if R_a > R_b:
        flag = flag + "0010"
    elif R_a < R_b:
        flag = flag + "0100"
    elif R_a == R_b:
        flag = flag + "0001"

    rpc["FLAGS"] = flag

    rpc["PC"] += 1
    return rpc, rt


# # TEST

# rpc = {
#         "R0": "0001010101010000",
#         "R1": "0000000000101000",
#         "R2": "0000000010011000",
#         "R3": "0000000000000010",
#         "R4": "0000000000000000",
#         "R5": "0000000000000000",
#         "R6": "0000000000000000",
#         "FLAGS":"0000000000000000",
#         "PC": 10
#     }
# rt = {
#         "R0": "int",
#         "R1": "int",
#         "R2": "int",
#         "R3": "int",
#         "R4": "int",
#         "R5": "int",
#         "R6": "int",
#         "FLAGS": 'int'
#     }

# rpcrt = cmp("0100000100001100",rpc, rt)
# rpc = rpcrt[0]
# rt = rpcrt[1]

# for key,value in rpc.items():
# 	print(key, ':', value)

# OUTPUT:

# R0 : 0000000000000000
# R1 : 0000000000000010
# R2 : 0000000010011000
# R3 : 0000000000000010
# R4 : 0000000000000000
# R5 : 0000000000000000
# R6 : 0000000000000000
# FLAGS : 0000000000000000
# PC : 11
