import argparse
import functools
import sys
from collections import namedtuple
from typing import List, NewType, Type
from src.data_triple import DataTriple

START_ADDRESS = 0x40

RR_CODES = dict(
    LR=0x00, LNR=0x01, STR=0x02, SWAPR=0x03, ANDR=0x04, ORR=0x05, RR=0x06,
    NOTR=0x07, BCSR=0x08, BCRR=0x09, BALR=0x0a, SACR=0x0b, CR=0x0c, CCS=0x0e,
    MCS=0x0f, AR=0x10, SR=0x11, RSR=0x12, MR=0x13, DR=0x14, RDR=0x15,
    REMR=0x16, RREMR=0x17, FAR=0x18, FSR=0x19, RFSR=0x1a, FMR=0x1b, FDR=0x1c,
    RFDR=0x1d, FLOATR=0x1e, FIXR=0x1f,
)

RS_CODES = dict(
    L=0x20, LN=0x21, ST=0x22, SWAP=0x23, AND=0x24, OR=0x25, XOR=0x26, NOT=0x27,
    BCS=0x28, BCR=0x29, BAL=0x2a, SAC=0x2b, C=0x2c, SVC=0x2e, A=0x30, S=0x31,
    RS=0x32, M=0x33, D=0x34, RD=0x35, REM=0x36, RREM=0x37, FA=0x38, FS=0x39,
    RFS=0x3a, FM=0x3b, FD=0x3c, RFD=0x3d, FLOAT=0x3e, FIX=0x3f, LA=0x4e,
    STM=0x6f, FLOOR=0x78, CEIL=0x79, MIN=0x7a, MAX=0x7b, SHIFTL=0x7c,
    SHIFTC=0x7d, SHIFTA=0x7e, SHIFTR=0x7f,
)

IM_CODES = dict(
    LI=0x40, LNI=0x41, ANDI=0x43, ORI=0x45, XORI=0x46, NOTI=0x47, CI=0x4c,
    AI=0x50, SI=0x51, RSI=0x52, MI=0x53, DI=0x54, RDI=0x55, REMI=0x56,
    RREMI=0x57, FAI=0x58, FSI=0x59, RFSI=0x5a, FMI=0x5b, FDI=0x5c, RFDI=0x5d,
    FLOATI=0x5e, FIXI=0x5f,
)

CH_CODES = dict(
    LC=0x60, LNC=0x61, STC=0x62, SWAPC=0x63, ANDC=0x64, ORC=0x65, XORC=0x66,
    NOTC=0x67, SACC=0x6b, CC=0x6c, AC=0x70, SC=0x71, RSC=0x72, MC=0x73,
    DC=0x74, RDC=0x75, REMC=0x76, RREMC=0x77
)

OP_CODES = dict()
OP_CODES.update(RS_CODES)
OP_CODES.update(RR_CODES)
OP_CODES.update(IM_CODES)
OP_CODES.update(CH_CODES)

Instruction = namedtuple('Instruction', ('opcode', 'operands'))


def strip_comment(line: str) -> str:
    if '#' in line:
        return line[:line.index('#')].strip()
    return line


def strip_comments(lines: List[str]) -> List[str]:
    return [strip_comment(l) for l in lines]


def parse_line(line: str) -> Instruction:
    instruction_name, *operands = map(str.strip, line.split(','))
    return Instruction(OP_CODES[instruction_name], operands)


def preprocess(lines: List[str]) -> List[str]:
    without_comments = strip_comments(lines)
    return without_comments


# TODO: rename to read_instructions
def read_source(file_object) -> List[Instruction]:
    raw_lines = preprocess(file_object.readlines())
    return list(parse_line(l.strip()) for l in raw_lines)


class UnsupportedOpCode(Exception):
    pass


class InvalidInstruction(Exception):
    pass


# TODO: rethink parameters
def to_data_triples(instruction, previous_address=-1):
    if instruction.opcode in set(RS_CODES.values()):
        r1, address = map(lambda x: int(x, 0), instruction.operands[0].split())
        r2 = int(instruction.operands[1])
        if not (r1 < 0x10 and r2 < 0x10):
            raise InvalidInstruction(
                "Register address should be a number between 0x0 and 0xf"
                "r1 = {:#x} r2 = {:#x}".format(r1, r2))
        address_left, address_right = address >> 8, (address & 0xff)
        data = [instruction.opcode,
                (r1 << 4) | r2, address_left, address_right]
    elif instruction.opcode in set(IM_CODES.values()):
        r1, value = map(lambda x: int(x, 0), instruction.operands[0].split())
        data = [instruction.opcode, r1 << 4 | (value & 0xf0000),
                value & 0xff00,
                value & 0xff]
    else:
        raise UnsupportedOpCode(f"{instruction.opcode} is not supported")
    return DataTriple(len(data), previous_address + 1, data)


def generate_record(data_triples, index=0):
    raw_record = f"{index:03x}{''.join(map(str, data_triples))}"
    checksum = sum(map(lambda x: int(x, 16), raw_record)) % 16
    return f"{checksum:x}{raw_record}".upper()


# TODO: optimize ALF generation by:
#  - scanning all records and joining contiguous memory segments
#  - removing duplicates
# TODO: make it work for many data triples
def data_triples_to_alf(data_triples):
    # TODO: split data triples into several records
    alf_lines = []
    try:
        record_line = generate_record(data_triples)
        # split records into 80 characters long parts
        alf_lines.append(record_line)
    except Exception as e:
        print("{}".format(e))

    alf_lines.append(f"END{START_ADDRESS:04x}")

    return '\n'.join(alf_lines).upper()


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
    # TODO: refactor it and write test
    start_address = 0x3f
    data_triples = []
    for instr in source:
        dt = None
        try:
            dt = to_data_triples(instr, start_address)
        except InvalidInstruction as e:
            print(e)
            sys.exit(1)
        data_triples.append(dt)
        start_address += dt.count
        start_address += int(start_address % 2 == 0)
    print(data_triples_to_alf(data_triples))
