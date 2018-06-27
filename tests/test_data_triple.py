import asm


def test_instruction_is_converted_properly():
    svc_instruction = asm.Instruction(0x2e, ['1 0', '1'])
    converted = asm.to_data_triples(svc_instruction)
    expected = asm.DataTriple(4, 0, [0x2e, (0x01 << 4) | 0x01, 0x00, 0x00])
    assert expected == converted
