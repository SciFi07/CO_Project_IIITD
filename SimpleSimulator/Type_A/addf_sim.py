# addf reg0 reg1 reg2=00000 00 000 001 010
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

def ieee_754_conversion(n, sgn_len=0, exp_len=3, mant_len=5):
    if n >= 2 ** (sgn_len + exp_len + mant_len):
        raise ValueError("Number n is longer than prescribed parameters allows")

    sign = (n & (2 ** sgn_len - 1) * (2 ** (exp_len + mant_len))) >> (exp_len + mant_len)
    exponent_raw = (n & ((2 ** exp_len - 1) * (2 ** mant_len))) >> mant_len
    mantissa = n & (2 ** mant_len - 1)

    sign_mult = 1
    if sign == 1:
        sign_mult = -1

    if exponent_raw == 2 ** exp_len - 1:  # Could be Inf or NaN
        if mantissa == 2 ** mant_len - 1:
            return float('nan')  # NaN

        # return sign_mult * float('inf')  # Inf

    exponent = exponent_raw - (2 ** (exp_len - 1) - 1)

    if exponent_raw == 0:
        mant_mult = 0  # Gradual Underflow
    else:
        mant_mult = 1

    for b in range(mant_len - 1, -1, -1):
        if mantissa & (2 ** b):
            mant_mult += 1 / (2 ** (mant_len - b))

    return (sign_mult * (2 ** exponent) * mant_mult)/2

def addf_instruction(instruct, reg, reg_type):
    if instruct[:5] != "10000":
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
            if reg_type[key] == 'int':
                return "ERROR:REGISTER WITH INT VALUE"
        if register[key] == instruct[13:]:
            cz = 1
            key3 = key
            if reg_type[key] == 'int':
                return "ERROR:REGISTER WITH INT VALUE"
    if cx == 0 or cy == 0 or cz == 0:
        return "ERROR:INVALID REGISTER"

    x = int(reg[key2], 2)
    x_f = ieee_754_conversion(x, exp_len=3, mant_len=5)
    y = int(reg[key3], 2)
    y_f = ieee_754_conversion(y, exp_len=3, mant_len=5)
    z = x_f + y_f
    if z > 16.0:
        # a = bin(z)[2:]
        # b = len(a) - 16
        # a = a[b:]
        reg["FLAGS"] = "0000000000001000"
        # reg[key1] = a
        reg[key1] = '0' * 16
        reg_type[key1] = 'int'
        reg["PC"] = reg["PC"] + 1
        return reg, reg_type
    z_f = format(reverse_ieee_754_conversion(z), "08b")
    l = 16 - len(str(z_f))
    reg[key1] = '0'*l + str(z_f)
    reg_type[key1] = 'float'
    reg["PC"] = reg["PC"] + 1
    return reg, reg_type


# test
# rpc = {
#         "R0": "0000000000000000",
#         "R1": "0000000011010010",
#         "R2": "0000000011010010",
#         "R3": "0000000000000010",
#         "R4": "0000000000000000",
#         "R5": "0000000000000000",
#         "R6": "0000000000000000",
#         "FLAGS":"0000000000000000",
#         "PC": 10
#     }
# rt = {
#         "R0": "int",
#         "R1": "float",
#         "R2": "float",
#         "R3": "int",
#         "R4": "int",
#         "R5": "int",
#         "R6": "int",
#         "FLAGS": 'int'
#     }

# print(addf_instruction("1000000000001010",rpc, rt))
