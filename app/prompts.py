import os

with open(os.path.join(os.path.dirname(__file__), "system_instruction.txt"), "r") as f:
    SYSTEM_INSTRUCTION = f.read()
