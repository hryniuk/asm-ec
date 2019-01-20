import json

# TODO: make it save it to file

JSON_FILE='./instructions.json'
FORMATS = ['RR', 'RS', 'IM', 'CH']

def format_instr(instr):
    code = hex(instr['code'])
    return f'''
### {instr['name']}
* `{code}`
* `{instr['syntax']}`
* `{instr['cond']}`

{instr['desc']}
'''

def create_md(instructions_dict):
    print('''# Available instructions

Each described in format

```
### Name
* opcode
* syntax
* possible condition code bits affected

Description
```
    ''')
    for fmt in FORMATS:
        print(f'## {fmt} instructions')
        for instr in instructions_dict:
            if instr['format'] == fmt:
                print(format_instr(instr))

def format_instr_row(instr):
    code = hex(instr['code'])
    return f'''| {instr['name']} | `{code}` | `{instr['syntax']}` | `{instr['cond']}` |'''


def create_table(instructions_dict):
    header = '''# Instructions
| name | opcode | syntax | poss. condition bits affected|
|------|--------|--------|----------------|'''
    print(header)
    for fmt in FORMATS:
        for instr in instructions_dict:
            if instr['format'] == fmt:
                print(format_instr_row(instr))

def main():
    with open(JSON_FILE) as f:
        instr_dict = json.loads(f.read())
        # create_md(instr_dict)
        create_table(instr_dict)

if __name__ == '__main__':
    main()
