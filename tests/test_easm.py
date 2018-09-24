from asm import strip_comments
from typing import List, NewType, Type


def str_to_list(source: str) -> List[str]:
    return source.split('\n')

def list_to_str(lines: List[str]) -> str:
    return '\n'.join(lines)

def test_preprocessing_removes_comments():
    source = '''
# newline comment
LI,0x0 0x05  # comment # still comment
LI,0x1 0x01
# commented code
# SVC,0x0 0x08,0
SVC,0x0 0x04,0
'''
    expected ='''

LI,0x0 0x05
LI,0x1 0x01


SVC,0x0 0x04,0
'''

    assert str_to_list(expected) == strip_comments(str_to_list(source))

