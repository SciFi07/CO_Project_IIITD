def je(instr, rfpc, rt):
    if instr[:5] != "11111":
        return "ERROR NOT JE"

    if rfpc["FLAGS"][-1] == "1":  # ET?
        rfpc["PC"] = int(instr[9:], 2)
    else:
        rfpc["PC"] += 1
    rfpc["FLAGS"] = "0" * 16  # flag reset
    return rfpc, rt
