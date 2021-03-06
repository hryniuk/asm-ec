import argparse
import functools
import sys
from collections import namedtuple
from typing import List, NewType, Type
from src.data_triple import DataTriple

START_ADDRESS = 0x40

RR_CODES = dict(
    LR=0x00,
    LNR=0x01,
    STR=0x02,
    SWAPR=0x03,
    ANDR=0x04,
    ORR=0x05,
    XORR=0x06,
    NOTR=0x07,
    BCRR=0x09,
    BALR=0x0A,
    SACR=0x0B,
    CR=0x0C,
    CCS=0x0E,
    MCS=0x0F,
    AR=0x10,
    SR=0x11,
    RSR=0x12,
    MR=0x13,
    DR=0x14,
    RDR=0x15,
    REMR=0x16,
    RREMR=0x17,
    FAR=0x18,
    FSR=0x19,
    RFSR=0x1A,
    FMR=0x1B,
    FDR=0x1C,
    RFDR=0x1D,
    FLOATR=0x1E,
    FIXR=0x1F,
)

RRM_CODES = dict(BCSR=0x08)

RS_CODES = dict(
    L=0x20,
    LN=0x21,
    ST=0x22,
    SWAP=0x23,
    AND=0x24,
    OR=0x25,
    XOR=0x26,
    NOT=0x27,
    BCS=0x28,
    BCR=0x29,
    BAL=0x2A,
    SAC=0x2B,
    C=0x2C,
    SVC=0x2E,
    A=0x30,
    S=0x31,
    RS=0x32,
    M=0x33,
    D=0x34,
    RD=0x35,
    REM=0x36,
    RREM=0x37,
    FA=0x38,
    FS=0x39,
    RFS=0x3A,
    FM=0x3B,
    FD=0x3C,
    RFD=0x3D,
    FLOAT=0x3E,
    FIX=0x3F,
    LA=0x4E,
    STM=0x6F,
    FLOOR=0x78,
    CEIL=0x79,
    MIN=0x7A,
    MAX=0x7B,
    SHIFTL=0x7C,
    SHIFTC=0x7D,
    SHIFTA=0x7E,
    SHIFTR=0x7F,
)

IM_CODES = dict(
    LI=0x40,
    LNI=0x41,
    ANDI=0x44,
    ORI=0x45,
    XORI=0x46,
    NOTI=0x47,
    CI=0x4C,
    AI=0x50,
    SI=0x51,
    RSI=0x52,
    MI=0x53,
    DI=0x54,
    RDI=0x55,
    REMI=0x56,
    RREMI=0x57,
    FAI=0x58,
    FSI=0x59,
    RFSI=0x5A,
    FMI=0x5B,
    FDI=0x5C,
    RFDI=0x5D,
    FLOATI=0x5E,
    FIXI=0x5F,
)

CH_CODES = dict(
    LC=0x60,
    LNC=0x61,
    STC=0x62,
    SWAPC=0x63,
    ANDC=0x64,
    ORC=0x65,
    XORC=0x66,
    NOTC=0x67,
    SACC=0x6B,
    CC=0x6C,
    AC=0x70,
    SC=0x71,
    RSC=0x72,
    MC=0x73,
    DC=0x74,
    RDC=0x75,
    REMC=0x76,
    RREMC=0x77,
)

OP_CODES = dict()
OP_CODES.update(RS_CODES)
OP_CODES.update(RRM_CODES)
OP_CODES.update(RR_CODES)
OP_CODES.update(IM_CODES)
OP_CODES.update(CH_CODES)

Instruction = namedtuple("Instruction", ("opcode", "operands"))


def strip_comment(line: str) -> str:
    if "#" in line:
        return line[: line.index("#")].strip()
    return line


def strip_comments(lines: List[str]) -> List[str]:
    return [strip_comment(l) for l in lines]


def remove_empty(lines: List[str]) -> List[str]:
    return [l for l in lines if len(l.strip()) > 0]


def parse_line(line: str) -> Instruction:
    instruction_name, *operands = map(str.strip, line.split(","))
    return Instruction(OP_CODES[instruction_name], operands)


def preprocess(lines: List[str]) -> List[str]:
    without_comments = strip_comments(lines)
    non_empty = remove_empty(without_comments)
    return non_empty


# TODO: rename to read_instructions
# TODO: add data format parser to detect syntax errors
def read_source(file_object) -> List[Instruction]:
    raw_lines = preprocess(file_object.readlines())
    return list(parse_line(l.strip()) for l in raw_lines)


class UnsupportedOpCode(Exception):
    pass


class InvalidInstruction(Exception):
    pass


# TODO: rethink parameters
def to_data_triples(instruction, previous_address=-1):
    # data contains characters to be written to the EC memory
    # i.e. data of DataTriple
    data = None
    if instruction.opcode in set(RRM_CODES.values()):
        m1, r2 = map(lambda x: int(x, 0), instruction.operands[0].split())
        if not r2 < 0x10:
            raise InvalidInstruction(
                "Register number should be between 0x0 and 0xf " "r2 = {:#x}".format(r2)
            )
        data = [instruction.opcode, (m1 << 4) | r2]
    elif instruction.opcode in set(RS_CODES.values()) or instruction.opcode in set(
        CH_CODES.values()
    ):
        r1, address = map(lambda x: int(x, 0), instruction.operands[0].split())
        r2 = int(instruction.operands[1])
        if not (r1 < 0x10 and r2 < 0x10):
            raise InvalidInstruction(
                "Register number should be between 0x0 and 0xf"
                "r1 = {:#x} r2 = {:#x}".format(r1, r2)
            )
        address_left, address_right = address >> 8, (address & 0xFF)
        data = [instruction.opcode, (r1 << 4) | r2, address_left, address_right]
    elif instruction.opcode in set(IM_CODES.values()):
        r1, value = map(lambda x: int(x, 0), instruction.operands[0].split())
        if not (r1 < 0x10):
            raise InvalidInstruction(
                "Register number should be between 0x0 and 0xf" "r1 = {:#x}".format(r1)
            )
        data = [
            instruction.opcode,
            (r1 << 4) | ((value & 0xF0000) >> 16),
            (value & 0xFF00) >> 8,
            value & 0xFF,
        ]
    elif instruction.opcode in set(RR_CODES.values()):
        r1, r2 = map(lambda x: int(x, 0), instruction.operands[0].split())
        if not (r1 < 0x10 and r2 < 0x10):
            raise InvalidInstruction(
                "Register number should be between 0x0 and 0xf"
                "r1 = {:#x} r2 = {:#x}".format(r1, r2)
            )
        data = [instruction.opcode, (r1 << 4) | r2]
    else:
        raise UnsupportedOpCode(f"{instruction.opcode} is not supported")
    assert data is not None
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

    return "\n".join(alf_lines).upper()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert EC assembly to an ALF")
    parser.add_argument("--asm-file", help="assembly file's path", required=False)

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
    start_address = 0x3F
    data_triples = []
    # TODO: process pair (intruction, source_line)
    # instead of instruction only to ease debugging
    for instr in source:
        dt = None
        try:
            dt = to_data_triples(instr, start_address)
        except InvalidInstruction as e:
            print(e)
            sys.exit(1)
        except ValueError as e:
            print("error on instruction {}:".format(instr))
            print(e)
            sys.exit(1)
        data_triples.append(dt)
        start_address += dt.count
        start_address += int(start_address % 2 == 0)
    print(data_triples_to_alf(data_triples))
