# mov reg0 $100 = 00010 0 000 1100100
# mov reg0 reg1 = 00011 00000 000 001
def mov(instruct, reg, rt):
    if instruct[:5] != "00010" and instruct[:5] != "00011":
        return "ERROR:ILLEGAL INSTRUCTION"

    list = ["000", "001", "010", "011", "100", "101", "110", "111"]
    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
        "FLAGS": "111",
    }

    if instruct[:5] == "00011":
        cx, cy = 0, 0
        for i in register:
            if instruct[10:13] == register[i]:
                cx = 1
                key1 = i
            if instruct[13:] == register[i]:
                cy = 1
                key2 = i
                if rt[i] == 'float':
                    return "ERROR:REGISTER WITH FLOAT VALUE"
        if cx == 0 or cy == 0:
            return "ERROR:INVALID REGISTER"
        reg[key1] = reg[key2]
        rt[key1] = 'int'
        reg["PC"] = reg["PC"] + 1
        reg["FLAGS"] = "0" * 16
        return reg, rt

    else:
        for i in register:
            if instruct[6:9] == register[i]:
                key = i
        reg[key] = "000000000" + instruct[9:]
        rt[key] = 'int'
        reg["PC"] = reg["PC"] + 1
        reg["FLAGS"] = "0" * 16
        return reg, rt


# test
# rpc = {
#         "R0": "0000000000000000",
#         "R1": "0000000000000011",
#         "R2": "0000000000000001",
#         "R3": "0000000000000010",
#         "R4": "0000000000000000",
#         "R5": "0000000000000000",
#         "R6": "0000000000000000",
#         "FLAGS":"0000000000000000",
#         "PC": 10
#     }

# print(mov("0001000001100100",rpc))
# print(mov("0001100000000001",rpc))
