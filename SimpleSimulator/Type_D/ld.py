def ld(inst, rfpc, rt, memobj):
    rfpc["FLAGS"] = "0" * 16
    rfpc["PC"] += 1
    rfpc["R" + str(int(inst[6:9], 2))] = memobj.inst_mem[int(inst[9:], 2)]
    # print(inst)
    # print(rfpc["R" + str(int(inst[6:9], 2))])
    # print(memobj.inst_mem[int(inst[9:], 2)])
    # print(rfpc)
    return rfpc, rt
