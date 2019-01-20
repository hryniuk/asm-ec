# asm-ec

[![Travis CI](https://img.shields.io/travis/hryniuk/asm-ec.svg?style=for-the-badge)](https://travis-ci.org/hryniuk/asm-ec)

# WORK IN PROGRESS

This project consist of two programs:
* **assembler** (see below) for the [The Educational Computer, Model 1 (EC)](https://github.com/hryniuk/ec)
* **loader** (see below) for the [The Educational Computer, Model 1 (EC)](https://github.com/hryniuk/ec)

## Usage

### Assembler

```shell
usage: asm.py [-h] [--asm-file ASM_FILE]

Convert EC assembly to an ALF

optional arguments:
  -h, --help           show this help message and exit
  --asm-file ASM_FILE  assembly file's path
```

### Linker

TBD

## About

### Assembler

The **assembler** transforms **assembly** code into **ALF** that can be run on
[EC](https://github.com/hryniuk/ec).


### Assembly

Assembly code consists of lines with instructions (see
[docs/instructions.md](docs/instructions.md)), at most one instruction per
line. Moreover each line may also include a comment, which is a fragment
starting from the `#` character.

A lot of examples (used as test files) can be found under `tests/` (EC assembly
file should end with `.easm` string).

#### Simple example

```
# set r0 to 5
LI,0x0 0x05

# Supervisor call with id = r0 = 5, i.e.
# write character at address 0x20 to the stdout
SVC,0x0 0x20,1 # writes 0, cause the whole memory is zeroed on EC start
```

### Loader

TBD

### MIT License

Copyright (c) 2018-2019 Łukasz Hryniuk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
