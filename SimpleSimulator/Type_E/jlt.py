def jlt(instr, rfpc):
    if instr[:5] != "11100":
        return "ERROR NOT JLT"

    if rfpc["FLAGS"][-3] == "1":  # LT?
        rfpc["PC"] = int(instr[9:], 2)
    else:
        rfpc["PC"] += 1
    rfpc["FLAGS"] = "0" * 16  # flag reset
    return rfpc
