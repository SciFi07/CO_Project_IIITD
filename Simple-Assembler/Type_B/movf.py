import math
def reverse_ieee_754_conversion(f, exp_len=3, mant_len=5):
    if abs(f) == float('inf'):
        exponent_bits = 2 ** exp_len - 1
        mantissa_bits = 0 if f >= 0 else 2 ** mant_len - 1
    elif abs(f) == float('nan'):
        exponent_bits = 2 ** exp_len - 1
        mantissa_bits = 2 ** mant_len - 1
    else:
        exponent = 0
        mantissa = 0

        if f != 0:
            exponent = int(math.log(abs(f), 2))
            mantissa = abs(f) / (2 ** exponent) - 1

        exponent += (2 ** (exp_len - 1) - 1)
        exponent_bits = exponent + 1
        mantissa_bits = int(mantissa * (2 ** mant_len))
    n = (exponent_bits << mant_len) | mantissa_bits
    return n

def movf(movf_instruction):
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
    list = movf_instruction.split()
    if len(list) != 3:
        return "ERROR: INCORRECT NUMBER OF OPERANDS"
    else:
        bin_string = "10010"

        if list[2][0] != "$":
            return "ERROR: INVALID OPERAND"
        list[2] = list[2][1:]

        try:
            num = float(list[2])
            if num > 16.0 or num < 1.0:
                return f"ERROR: {num} CANNOT BE USED AS AN IMMEDITATE VALUE"
            for i in register:
                if i == list[1] and i != "FLAGS":
                    bin_string = bin_string + register[i]
                    break
                elif i == "FLAGS":
                    return "ERROR: IMMEDITATE VALUES CANNOT BE WRITTEN TO FLAGS"
            else:
                return "ERROR: INVALID REGISTER CODE"
            num = reverse_ieee_754_conversion(num, exp_len=3, mant_len=5)
            bin_string = bin_string + format(num, "08b")
            return bin_string
        except:
            return "ERROR: THIS INSTRUCTION ONLY TAKES POSITIVE FLOATING TYPE NUMBERS"


# instruct="mov R1 $12.25"
# print(movf(instruct))
