"""
fconv contains set of functions doing the same as their correspondent
in fconv of ec (https://github.com/hryniuk/ec) project, i.e.

converting float32 to array of u8 values (in Python int values in u8 value range)
and vice-versa
"""
import struct

STRUCT_FMT = ">f"


def float32_to_bytes(v):
    # Note: explicitly converting to float as it do not change behaviour, i.e.
    # float32_to_bytes(float(<int>)) == float32_to_bytes(<int>)
    # ...but might help in debugging.
    return list(struct.pack(STRUCT_FMT, float(v)))


def bytes_to_float32(b):
    return struct.unpack(STRUCT_FMT, bytes(b))


def float20_to_bytes(v):
    # Note: see comment in float32_to_bytes.
    r = float32_to_bytes(v)
    r[3] = r[3] & 0xF0
    return r


def bytes_to_float20(b):
    assert (b[3] & 0x0F) == 0
    return struct.unpack(STRUCT_FMT, bytes(b))
