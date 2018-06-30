from asm import DataTriple, generate_record


def test_alf_is_generated_properly():
    expected = 'E10241A2301020304207FF1BEC'
    data_triples = [DataTriple(4, 0x1a23, [0x01, 0x02, 0x03, 0x04]),
                    DataTriple(2, 0x07ff, [0x1b, 0xec])]

    generated = generate_record(data_triples, 0x102)

    assert len(generated) <= 80
    assert expected == generated
