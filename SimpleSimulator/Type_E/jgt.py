def jgt(instr, rfpc, rt):
    if instr[:5] != "11101":
        return "ERROR NOT JGT"

    if rfpc["FLAGS"][-2] == "1":  # GT?
        rfpc["PC"] = int(instr[9:], 2)
    else:
        rfpc["PC"] += 1
    rfpc["FLAGS"] = "0" * 16  # flag reset
    return rfpc, rt
