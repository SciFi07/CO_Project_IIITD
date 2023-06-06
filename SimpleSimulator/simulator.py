import sys
import warnings

from parsets import IMACC, PROGC, REGFLPC, ExecE 

warnings.filterwarnings("ignore")

MEM = IMACC(sys.stdin.read())  # Load memory from stdin
PC = PROGC(0)  # Start from the first instruction
RF = REGFLPC()  # initialize register and flags
reg_type = {
        "R0": "int",
        "R1": "int",
        "R2": "int",
        "R3": "int",
        "R4": "int",
        "R5": "int",
        "R6": "int",
        "FLAGS":"int",
    }
EE = ExecE(MEM)
halted = False
cycle = 0

if MEM.inst_mem == ["0" * 16 for i in range(128)]:
    halted = True

while not halted:
    Instruction = MEM.getData(PC)  # Get current instruction
    halted, new_PC, new_regs, reg_type = EE.execute(Instruction, RF.asdct(), reg_type)
    # Update RF compute new_PC
    RF.update(new_regs, new_PC)
    PC.dump()
    # Print PC
    RF.dump()
    # Print RF state
    PC.update(new_PC)
    # Update PC
    cycle += 1

MEM.dump()  # Print memory state

