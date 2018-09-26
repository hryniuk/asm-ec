import asm


def test_rs_instruction_is_converted_properly():
    svc_instruction = asm.Instruction(0x2e, ["1 0", "1"])
    converted = asm.to_data_triples(svc_instruction)
    expected = asm.DataTriple(4, 0, [0x2e, (0x01 << 4) | 0x01, 0x00, 0x00])
    assert expected == converted


def test_rr_instruction_is_converted_properly():
    rr_instruction = asm.Instruction(0x13, ["1 2"])
    converted = asm.to_data_triples(rr_instruction)
    expected = asm.DataTriple(2, 0, [0x13, (0x01 << 4) | 0x02])
    assert expected == converted


def test_im_instruction_is_converted_properly():
    im_instruction = asm.Instruction(0x40, ["0x9 0xfedce"])
    converted = asm.to_data_triples(im_instruction)
    expected = asm.DataTriple(4, 0, [0x40, (0x9 << 4) | 0xf, 0xed, 0xce])
    assert expected == converted


def test_data_triple_is_formatted_correctly():
    dt = asm.DataTriple(4, 0, [0x2e, 0x05 << 4, 0x00, 0x20])
    assert str(dt) == "400002e500020"
