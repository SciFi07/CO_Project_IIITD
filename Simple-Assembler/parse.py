# Parser for A,B,C,D,E,F
import re

from Type_A import add, sub, mul, XOR, OR, AND, addf, subf
from Type_B import mov, Lshift, Rshift, movf
from Type_C import div, Compare, Invert
from Type_D import ld, st
from Type_E import je, jgt, jlt, jmp


def parser(string, labels, variables):
    # TODO
    parsed_string = ""

    break_string = string.split()
    if break_string == []:
        return "ERROR: LABEL WAS NOT FOLLOWED BY AN INSTRUCTION"
    op = break_string[0]

    if op == "hlt":
        return "1101000000000000"
    elif op == "add":
        parsed_string = add(string)
    elif op == "addf":
        parsed_string = addf(string)
    elif op == "sub":
        parsed_string = sub(string)
    elif op == "subf":
        parsed_string = subf(string)
    elif op == "mul":
        parsed_string = mul(string)
    elif op == "div":
        parsed_string = div(string)
    elif op == "mov":
        parsed_string = mov(string)
    elif op == "movf":
        parsed_string = movf(string)
    elif op == "and":
        parsed_string = AND(string)
    elif op == "cmp":
        parsed_string = Compare(string)
    elif op == "not":
        parsed_string = Invert(string)
    elif op == "ls":
        parsed_string = Lshift(string)
    elif op == "rs":
        parsed_string = Rshift(string)
    elif op == "or":
        parsed_string = OR(string)
    elif op == "xor":
        parsed_string = XOR(string)
    elif op == "jgt":
        parsed_string = jgt(string, labels)
    elif op == "ld":
        parsed_string = ld(string, variables)
    elif op == "st":
        parsed_string = st(string, variables)
    elif op == "jmp":
        parsed_string = jmp(string, labels)
    elif op == "jlt":
        parsed_string = jlt(string, labels)
    elif op == "je":
        parsed_string = je(string, labels)
    elif op == "var":
        parsed_string = "ERROR: VARIABLE CANNOT BE DECLARED INSIDE LABELS"
    elif re.match("\s*[A-Za-z0-9]+:.*", op):
        parsed_string = "ERROR: LABEL FOUND INSIDE LABEL"
    else:
        parsed_string = "ERROR: WRONG MNENOMIC >> " + string

    return parsed_string
