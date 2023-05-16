# je


def je(string, labels):

    arr = string.split()
    output = "11111"
    err = ""

    lbdct = {i[0]: i[1] for i in labels}
    if len(arr) == 2:
        output = output + "0000"
        if lbdct.get(arr[1]) is not None:
            mem = lbdct.get(arr[1])
            output = output + bin(mem)[2:].zfill(7)
            return output
        else:
            err = "ERROR: LABEL WAS NOT FOUND"
            return err

    else:
        err = "ERROR: INVALID NUMBER OF ARGUMENTS"
        return err
