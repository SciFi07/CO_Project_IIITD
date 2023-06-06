def jmp(instr, rfpc, rt):
    if instr[:5] != "01111":
        return "ERROR NOT JMP"

    rfpc["FLAGS"] = "0" * 16
    rfpc["PC"] = int(instr[9:], 2)
    return rfpc, rt
