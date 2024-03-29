def sub_instruction(instruct, reg, reg_type):
    if instruct[:5] != "00001":
        return "ERROR:ILLEGAL INSTRUCTION"

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
    if (
        instruct[7:10] == register["FLAGS"]
        or instruct[10:13] == register["FLAGS"]
        or instruct[13:] == register["FLAGS"]
    ):
        return "ERROR:FLAG REGISTER WAS ACCESSED"

    reg["FLAGS"] = "0" * 16

    cx, cy, cz = 0, 0, 0

    for key in register:
        if register[key] == instruct[7:10]:
            cx = 1
            key1 = key
        if register[key] == instruct[10:13]:
            cy = 1
            key2 = key
            if reg_type[key] == 'float':
                return "ERROR:REGISTER WITH FLOAT VALUE"
        if register[key] == instruct[13:]:
            cz = 1
            key3 = key
            if reg_type[key] == 'float':
                return "ERROR:REGISTER WITH FLOAT VALUE"
    if cx == 0 or cy == 0 or cz == 0:
        return "ERROR:INVALID REGISTER"
    x = int(reg[key2], 2)
    y = int(reg[key3], 2)
    z = x - y
    if z < 0:
        z = 0
        reg["FLAGS"] = "0000000000001000"
        reg[key1] = format(z, "016b")
        reg["PC"] = reg["PC"] + 1
        return reg, reg_type

    reg[key1] = format(z, "016b")
    reg["PC"] = reg["PC"] + 1
    return reg, reg_type


# teat
# rpc = {
#     "R0": "0000000000000000",
#     "R1": "0000000000000000",
#     "R2": "000000000000001",
#     "R3": "0000000000000011",
#     "R4": "0000000000000000",
#     "R5": "0000000000000000",
#     "R6": "0000000000000000",
#     "FLAGS":"0000000000000000",
#     "PC": 10
# }

# print(sub_instruction("0000100001010011",rpc))
