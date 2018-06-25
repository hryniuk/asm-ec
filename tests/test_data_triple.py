import asm


def test_instruction_is_converted_properly():
    svc_instruction = asm.Instruction(0x2e, ['1 0', '1'])
    converted = asm.to_data_triples(svc_instruction)
    expected = [asm.DataTriple(1, 0, 0x2e),
                asm.DataTriple(1, 1, (0x01 << 4) | 0x01),
                asm.DataTriple(1, 2, 0x00),
                asm.DataTriple(1, 3, 0x00)]
    assert len(expected) == len(converted)
    assert all(expected.count(x) == converted.count(x) for x in expected)
