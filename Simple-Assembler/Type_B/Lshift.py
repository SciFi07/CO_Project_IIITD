def Lshift(str_in):

    arr = str_in.split()
    output = "010010"
    err = ""
    if "FLAGS" in arr:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"

    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
    }

    rlist = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

    if len(arr) == 3:
        if arr[1] == "FLAGS":
            err = "ERROR: INVALID USE OF FLAGS"
            return err
        if arr[1] in rlist:
            output = output + register.get(arr[1])
        else:
            err = "ERROR: INVALID REGISTER CODE"
            return err

        imm = arr[2]

        if imm[0] == "$":

            imm = int(imm[1 : len(imm)])

            if imm in range(128):
                imm_bin = str(bin(imm))
                imm_bin = imm_bin[2 : len(imm_bin)]
                if len(imm_bin) < 7:
                    imm_bin = (7 - len(imm_bin)) * "0" + imm_bin
                output = output + imm_bin
            else:
                err = "ERROR: IMMIDIATE OUT OF BOUND"
                return err

        else:
            err = "ERROR: INVALID IMMIDIATE INPUT"
            return err

        return output

    else:
        err = "ERROR: INVALID NUMBER OF ARGUMENTS"
        return err


# TEST
# s_in = "ls R1 $0"
# print(Lshift(s_in))
# output = 010010 001 0000 0000

