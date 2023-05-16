import re
import sys

from parse import parser

variables = []
labels = []

run = True


def varproc(string):
    global variables
    inst = string.split()
    if not (len(inst) == 2):
        return "[91m" + "ERROR:" + "[0m" + " INVALID VARIABLE DECLARATION"
    # if var name is pure numbers
    if re.match("^[0-9]+$", inst[1].strip()):
        return "[91m" + "ERROR:" + "[0m" + " VARIABLE NAME PURELY NUMERIC"
    if re.match(".*[^A-Za-z0-9_]+", inst[1]):
        return "[91m" + "ERROR:" + "[0m" + " INVALID VARIABLE NAME"
    if inst[1] in {
        "var",
        "add",
        "sub",
        "mov",
        "ld",
        "st",
        "mul",
        "div",
        "rs",
        "ls",
        "xor",
        "or",
        "and",
        "not",
        "cmp",
        "jmp",
        "jlt",
        "jgt",
        "je",
        "hlt",
        "R1",
        "R2",
        "R3",
        "R4",
        "R5",
        "R6",
        "R0",
        "FLAGS",
    }:
        return (
            "[91m"
            + "ERROR:"
            + "[0m"
            + f" VARIABLE NAME SAME AS KEYWORD KNOWN IN ISA >> {inst[1].strip()}"
        )
    # second needs to be regexed
    # append to variable storage(address after instruction mem is made)
    variables.append([inst[1], 0])  # stored variable (not addressed)
    return None


def labelproc(string):
    # here string is always a valid label
    global labels
    if re.match("\s*[0-9]+$", string[: string.index(":")]):
        return "[91m" + "ERROR:" + "[0m" + " LABEL NAME PURELY NUMERIC"
    if string[: string.index(":")].lstrip() in {
        "var",
        "add",
        "sub",
        "mov",
        "ld",
        "st",
        "mul",
        "div",
        "rs",
        "ls",
        "xor",
        "or",
        "and",
        "not",
        "cmp",
        "jmp",
        "jlt",
        "jgt",
        "je",
        "hlt",
        "R1",
        "R2",
        "R3",
        "R4",
        "R5",
        "R6",
        "R0",
        "FLAGS",
    }:
        return (
            "[91m"
            + "ERROR:"
            + "[0m"
            + f" LABEL NAME SAME AS KEYWORD IN ISA >> {string.split()[0][:-1]}"
        )
    labels.append([string[: string.index(":")].strip(), proc1.index(string)])

    if len(set([i[0] for i in labels])) != len([i[0] for i in labels]):
        return (
            "[91m" + "ERROR:" + "[0m" + " MULTIPLE SAME NAME LABEL DECLARATION FOUND"
        )

    ninst = string[string.index(":") :].lstrip(":")
    proc1l[proc1.index(string)] = ninst
    return None


# files have been read to input stream using < command
# hence using stdin.read to read the whole stream together
assembly = sys.stdin.read()

run_1=True


if bool(re.match("\s*$", assembly)):
    print("ln: 0 --> " + "[91m" + "ERROR:" + "[0m" + " EMPTY STDIN OR NO INSTRUCTION")
    run_1 = False


# if run:
    # process each line of assembly
lines_assembly = assembly.split("\n")

    # ignore blank lines
proc1 = [l for l in lines_assembly if not re.match("^\s*$", l)]

run_2=True
while run_2:
    if proc1 == []:
        break
    if proc1[0].split()[0] == "var":
        if (e := varproc(ln := proc1.pop(0))) is not None:
            print(f"ln: {lines_assembly.index(ln)+1} --> " + e)
            run_2 = False
            break
    else:
        break

# now proc1 is free of variables (hopefully)
run_3=True
if any((j := re.match("\s*var\s.*", i)) for i in proc1):
    print(
        f"ln: {lines_assembly.index(j.string)+1} --> "
        + "[91m"
        + "ERROR:"
        + "[0m"
        + " VARIABLE NOT DECLARED AT START"
    )
    run_3 = False

# guaranteed proc1 only has instructions

if True:
    inst_len = len(proc1)
    for i in variables:
        i[1] = inst_len
        inst_len += 1

    # all variables now have address

    # now process for labels

    proc1l = proc1.copy()

run_4=True
if True:
    for i in proc1:
        if re.match("\s*[A-Za-z0-9_]+:.*", i):
            if (e := labelproc(i)) is not None:
                print(f"ln: {lines_assembly.index(i)+1} --> " + e)
                run_4 = False

run_5=True
run_6=True

if True:
    # check hlt instruction
    hlts = [
        l
        for l in lines_assembly
        if re.match("\s*hlt\s*", l) or re.match("[A-Za-z0-9]+:\s*hlt\s*", l)
    ]
    if len(hlts) > 1:
        print(
            f"ln: {lines_assembly.index(hlts[0])+1} --> "
            + "[91m"
            + "ERROR:"
            + "[0m"
            + " MULTIPLE HALT INSTRUCTIONS IN STDIN"
        )
        run_5 = False
    if len(hlts) == 1:
        if proc1.index(hlts[0]) != len(proc1) - 1:
            print(
                f"ln: {lines_assembly.index(hlts[0])+1} --> "
                + "[91m"
                + "ERROR:"
                + "[0m"
                + " HALT IS NOT LAST INSTRUCTION"
            )
            run_6 = False
        else:
            pass

run_7=True
run_8=True
if True:
    parsed = [parser(i.strip(), labels, variables) for i in proc1l]
    for i, e in enumerate(parsed):
        if e[0] != "0" and e[0] != "1":
            print(
                f"ln: {lines_assembly.index(proc1[i])+1} --> "
                + "\033[91m"
                + "ERROR:"
                + "\033[0m"
                + e[6:]
            )
            run_7 = False

    if parsed == [] or parsed[-1] != "1101000000000000":
        run_8 = False
        print(
            "ln: xx --> "
            + "\033[91m"
            + "ERROR:"
            + "\033[0m"
            + " HALT INSTRUCTION NOT FOUND"
        )

    ## if non_binary in parsed: print error
    ## else: create for loop and print binaries

if run_1 and run_2 and run_3 and run_4 and run_5 and run_6 and run_7 and run_8:
    print("\n".join(parsed))
