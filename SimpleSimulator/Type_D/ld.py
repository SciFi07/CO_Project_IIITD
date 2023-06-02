def ld(inst, rfpc, memobj):
    rfpc["FLAGS"] = "0" * 16
    rfpc["PC"] += 1
    rfpc["R" + str(int(inst[6:9], 2))] = memobj.inst_mem[int(inst[9:], 2)]
    return rfpc
