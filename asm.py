import argparse
import sys
from collections import namedtuple
from typing import List, NewType, Type
from src.data_triple import DataTriple

START_ADDRESS = 0xa

OP_CODES = dict(
    SVC=0x2e,
)

RS = {0x2e}

Instruction = namedtuple('Instruction', ('opcode', 'operands'))


def parse_line(line: str) -> Instruction:
    instruction_name, *operands = map(str.strip, line.split(','))
    return Instruction(OP_CODES[instruction_name], operands)


def read_source(file_object) -> List[Instruction]:
    return list(parse_line(l.strip()) for l in file_object.readlines())


def to_data_triples(instruction, previous_address=-1):
    if instruction.opcode in RS:
        r1, address = map(lambda x: int(x, 0), instruction.operands[0].split())
        r2 = int(instruction.operands[1])
        address_left, address_right = address >> 8, (address & 0xff)
        data = [instruction.opcode,
                (r1 << 4) | r2, address_left, address_right]
        return DataTriple(4, previous_address + 1, data)

    return None


def generate_record(data_triples, index=0):
    raw_record = f"{index:03x}{''.join(map(str, data_triples))}"
    checksum = sum(map(lambda x: int(x, 16), raw_record)) % 16
    return f"{checksum:x}{raw_record}".upper()


# TODO: optimize ALF generation by:
#  - scanning all records and joining contiguous memory segments
#  - removing duplicates
def data_triples_to_alf(data_triples):
    # TODO: split data triples into several records
    alf = generate_record(data_triples)
    assert len(alf) <= 80

    alf += "\n"
    alf += f"END{START_ADDRESS:04x}"

    return alf.upper()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert EC assembly to an ALF')
    parser.add_argument('--asm-file',
                        help="assembly file's path",
                        required=False)

    args = parser.parse_args()
    source = None
    try:
        with open(args.asm_file) as f:
            source = read_source(f)
    except FileNotFoundError:
        print(f"No such file: {args.asm_file}")
    except TypeError:
        source = read_source(sys.stdin)

    assert source is not None
    print(data_triples_to_alf(map(to_data_triples, source)))
