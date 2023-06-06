def movf(instruct, reg, rt):
    if instruct[:5] != "10010":
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
    for i in register:
        if instruct[5:8] == register[i]:
            key = i
    reg[key] = "00000000" + instruct[8:]
    rt[key] = 'float'
    reg["PC"] = reg["PC"] + 1
    reg["FLAGS"] = "0" * 16
    # print(instruct, reg, rt)
    # print("here")
    return (reg, rt)


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
