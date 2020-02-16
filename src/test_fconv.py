import src.fconv as fconv

# fn test_float32_to_bytes_conversion() {
#     assert_eq!(float32_to_bytes(3.5_f32), [0x40, 0x60, 0x00, 0x00]);
#     assert_eq!(float32_to_bytes(-789.3145_f32), [0xC4, 0x45, 0x54, 0x21]);
#     assert_eq!(float32_to_bytes(789.3145_f32), [0x44, 0x45, 0x54, 0x21]);
# }
# fn test_float20_to_bytes_conversion() {
#     assert_eq!(float20_to_bytes(3.5_f32), [0x40, 0x60, 0x00, 0x00]);
#     assert_eq!(float20_to_bytes(-789.3145_f32), [0xC4, 0x45, 0x54, 0x20]);
#     assert_eq!(float20_to_bytes(789.3145_f32), [0x44, 0x45, 0x54, 0x20]);
# }
# fn test_bytes_to_float32_conversion() {
#     approx::abs_diff_eq!(bytes_to_float32([0x40, 0x60, 0x00, 0x00]), 3.5_f32);
#     approx::abs_diff_eq!(bytes_to_float32([0xC4, 0x45, 0x54, 0x21]), -789.3145_f32);
#     approx::abs_diff_eq!(bytes_to_float32([0x44, 0x45, 0x54, 0x21]), 789.3145_f32);
# }
# fn test_bytes_to_float20_conversion() {
#     approx::abs_diff_eq!(bytes_to_float20([0x40, 0x60, 0x00, 0x00]), 3.5_f32);
#     approx::abs_diff_eq!(bytes_to_float20([0xC4, 0x45, 0x54, 0x20]), -789.3145_f32);
#     approx::abs_diff_eq!(bytes_to_float20([0x44, 0x45, 0x54, 0x20]), 789.3145_f32);
# }

# Apparently with current implementation it's not possible to get
# better precision than this.
EPS = 1e-4

float32_bytes_value_pairs = [
    [3.5, [0x40, 0x60, 0x00, 0x00]],
    [-789.3145, [0xC4, 0x45, 0x54, 0x21]],
    [789.3145, [0x44, 0x45, 0x54, 0x21]],
]

float20_bytes_value_pairs = [
    [3.5, [0x40, 0x60, 0x00, 0x00]],
    [-789.3145, [0xC4, 0x45, 0x54, 0x20]],
    [789.3145, [0x44, 0x45, 0x54, 0x20]],
]

int_bytes_value_pairs = [[]]


def approx_abs_diff_eq(x, y):
    return abs(x - y) < EPS


def test_float32_to_bytes_conversion():
    for value_bytes_pair in float32_bytes_value_pairs:
        if len(value_bytes_pair) != 2:
            assert False
        v, b = value_bytes_pair
        assert fconv.float32_to_bytes(v) == b


def test_float20_to_bytes_conversion():
    for value_bytes_pair in float20_bytes_value_pairs:
        if len(value_bytes_pair) != 2:
            assert False
        v, b = value_bytes_pair
        assert fconv.float20_to_bytes(v) == b


def test_bytes_to_float32_conversion():
    for value_bytes_pair in float32_bytes_value_pairs:
        if len(value_bytes_pair) != 2:
            assert False
        v, b = value_bytes_pair
        result = fconv.bytes_to_float32(b)
        assert len(result) == 1
        assert approx_abs_diff_eq(result[0], v)


def test_bytes_to_float20_conversion():
    for value_bytes_pair in float20_bytes_value_pairs:
        if len(value_bytes_pair) != 2:
            assert False
        v, b = value_bytes_pair
        result = fconv.bytes_to_float20(b)
        assert len(result) == 1
        assert approx_abs_diff_eq(result[0], v)
