def addf(addf_instruction):
    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
    }
    list = addf_instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) > 4:
        return "ERROR: MORE THAN THREE OPERANDS GIVEN"
    if len(list) < 4:
        return "ERROR: INCOMPLETE INSTRUCTION"
    if list[0] != "addf":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        c = 0
        bin_string = "1000000"
        for j in range(1, 4):
            for i in register:
                if i == list[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                return "ERROR: INVALID REGISTER CODE"
        return bin_string


# instruct="add R0 R1 R2 R5"
# print(add(instruct))
