import argparse
import sys
from collections import namedtuple
from typing import List, NewType, Type

START_ADDRESS = 0xa

OP_CODES = dict(
    SVC=0x2e,
)

RS = {'SVC'}

Instruction = namedtuple('Instruction', ('opcode', 'operands'))
DataTriple = namedtuple('DataTriple', ('count', 'address', 'data'))


def parse_line(line: str) -> Instruction:
    instruction_name, *operands = map(str.strip, line.split(','))
    return Instruction(OP_CODES[instruction_name], operands)


def read_source(file_object) -> List[str]:
    return list(parse_line(l.strip()) for l in file_object.readlines())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert EC assembly to an ALF')
    parser.add_argument('--asm-file',
                        help="assembly file's path",
                        required=False)

    args = parser.parse_args()
    try:
        with open(args.asm_file) as f:
            print(read_source(f))
            sys.exit(0)
    except FileNotFoundError:
        print(f"No such file: {args.asm_file}")
    except TypeError:
        print(read_source(sys.stdin))
