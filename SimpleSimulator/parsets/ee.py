from Type_A import *
from Type_B import *
from Type_C import *
from Type_D import *
from Type_E import *
from Type_F import *


class ExecE:

    # define a class variable only for MAC instructions and store access
    # might also need
    def __init__(self, memobj):
        self.mem = memobj

    def execute(self, inst16bit, rfpc, reg_type):
        if inst16bit[:5] == "00101":  # store
            self.mem.maintainvar(
                inst16bit[9:], rfpc.get("R" + str(int(inst16bit[6:9], 2)))
            )
            rfpc["PC"] += 1
            rfpc["FLAGS"] = "0000000000000000"
            return False, rfpc["PC"], rfpc, reg_type
        elif inst16bit[:5] == "11010":
            rfpc["FLAGS"] = "0000000000000000"
            return True, -1, rfpc, reg_type
        else:
            # print(rfpc, reg_type)
            rfpcrt = ExecE.parse(self, inst16bit, rfpc, reg_type)
            rfpc = rfpcrt[0]
            reg_type = rfpcrt[1]
            # print(rfpc, reg_type)
            return False, rfpc["PC"], rfpc, reg_type

    def parse(self, inst16bit, rfpc, reg_type):
        if inst16bit[:5] == "00000":
            # print(inst16bit)
            return add(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "10000":
            return addf(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "00001":
            return sub(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "10001":
            return subf(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "00010":
            return mov(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "10010":
            return movf(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "00011":
            return mov(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "00100":
            return ld(inst16bit, rfpc, reg_type, self.mem)  # add provision for mem view
        elif inst16bit[:5] == "00110":
            return mul(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "00111":
            return div(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01000":
            return rshift(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01001":
            return lshift(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01010":
            return xor(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01011":
            return OR(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01100":
            return AND(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01101":
            return invert(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01110":
            return cmp(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "01111":
            return jmp(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "11100":
            return jlt(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "11101":
            return jgt(inst16bit, rfpc, reg_type)
        elif inst16bit[:5] == "11111":
            return je(inst16bit, rfpc, reg_type)
