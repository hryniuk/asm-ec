# Available instructions

Each described in format

```
### Name
* opcode
* syntax
* possible condition code bits affected

Description
```

## RR instructions

### Load Register
* `0x0`
* `LR,R1 R2`
* `GLE`

The register R1 is loaded with the word at the effective address. The load value is compared with zero and the G, L, or E bit of the CCR set as appropriate. If the effective address does not fall on a word boundary, a word-addressing exception occurs.


### Load Negative Register
* `0x1`
* `LNR,R1 R2`
* `OGLE`

The register R1 is loaded with the two's complement of the word at the effective address. The loaded result is compared to zero to set the CCR. If overflow occurs, only the 0 bit of the CCR is set. A word-addressing exception may occur.


### Store Register
* `0x2`
* `STR,R1 R2`
* `GLE`

The value in R1 is stored in the word at the effective address. The stored value is compared to zero to set the CCR. A word-addressing exception may occur.


### Swap Register
* `0x3`
* `SWAPR,R1 R2`
* `GLE`

The word in register R1 is exchanged with the word at the effective address. The CCR is set by comparing the value moved into register R1 with zero. A word-addressing exception may occur.


### And Register
* `0x4`
* `ANDR,R1 R2`
* `GLE`

The logical and of the word in R1 and the word at the effective address is formed and loaded into register R1. Bit G of the CCR is set if the final value in R1 is all ones, bit L is set if the result if mixed zeros and ones, and bit E is set if the result is all zeros. A word-addressing exception may occur.


### Or Register
* `0x5`
* `ORR,R1 R2`
* `GLE`

This instruction operates in the same way as the And Register with logical or replacing logical and.


### Exclusive Or Register
* `0x6`
* `XORR,R1 R2`
* `GLE`

This instruction operates in the same way as And Register with logical and replaced by logical exclusive or.


### Not Register
* `0x7`
* `NOTR,R1 R2`
* `GLE`

This instruction operates in the same way as And Register with logical and replaced by logical complement of the second operand, the original value in register R1 being ignored.


### Branch Conditions Set Register
* `0x8`
* `BCSR,M1 R2`
* `None`

If the logical and of the contents of the CCR and the 4-bit logical mask M1 is nonzero, the contents of the ILC are replaced by the effective address.


### Branch Conditions Reset Register
* `0x9`
* `BCRR,M1 R2`
* `None`

If the logical and of the contents of the CCR and the 4-bit logical mask M1 is zero, the contents of the ILC are replaced by the effective address.


### Branch and Link Register
* `0xa`
* `BALR,R1 R2`
* `None`

The current contents of the ILC are loaded into register R1 and the effective address is loaded into the ILC. If the indirect bit is not on, the effective address is register designator R2 multiplied by 4.


### Save Condition Register
* `0xb`
* `SACR,M1 R2`
* `None`

If the logical and of the CCR and the 4-bit mask field M1 is nonzero, a word of all one bits is stored in the effective address; otherwise a word of all zeros is stored. A word-addressing exception may occur.


### Compare Register
* `0xc`
* `CR,R1 R2`
* `GLE`

The results of an algebraic comparison between the contents of register R1 and the word at the effective address are used to set the G, L, or E bits of the CCR as appropriate. A word-addressing exception may occur.


### Compare Character String
* `0xe`
* `CCS,M1 R2`
* `GLE`

Register designator R2 names a register pair R2 and (R2+1) mod 16 (the second register will be called R2+1 throughout). The pair R2 and R2+1 should contain a string descriptor doubleword, with a character address A1 in bits 16 through 31 of register R2, a length L in bits 0 through 15 of register R2+1, and a character address A2 in bits 16 through 31 of register R2+1. To begin execution, A1, A2, and L are moved to internal registers, the CCR is set to zero, and the E bit of the CCR is set to one. A loop is started.  First, if L is zero, bits 0 through 15 of both registers are set to zero, bits 16 to 31 of R2 are set to the internal value of A1, bits 16 through 31 of R2+1 are set to the internal value of A2, and the instruction terminates.  Second, the character of A1 is compared as an 8-bit integer to the character at A2 and the result used to set the appropriate bits of the CCR.  Third, if the E bit of the CCR is not one, bits 0 through 15 of register R2 are set to zero, bits 16 through 31 of R2 to the internal value of A1, bits 0 through 15 of R2+1 to the internal value of L, bits 16 through 31 of R2+1 to the internal value of A2, and the instruction terminates.  Finally, L is decremented by 1, A1 is incremented by the mask M1 interpreted as a 4-bit two's complement integer, and A2 is incremented by 1, and the loop returns to the first step.


### Move Character String
* `0xf`
* `MCS,M1 R2`
* `None`

Registers R2 and (R2+1) mod 16 contain a string descriptor doubleword as described in Compare Character String. The L, A1, and A2 fields are loaded into internal registers. A loop is begun.  First, if L is zero, bits 0 through 15 of registers R2 and R2+1 are set to zero, bits 16 through 31 of R2 to A1, bits 16 through 31 of R2+1 to A2, and the instruction terminates.  Second, the character at location A1 is stored at character location A2.  Third, L is decremented by 1 and A2 is incremented by 1.  Finally, A1 is incremented by the mask M1 interpreted as a 4-bit two's complement integer and the loop returns to its first step.


### Add Register
* `0x10`
* `AR,R1 R2`
* `OGLE`

The word in R1 is added to the word at the effective address and the result is placed in R1. The sum is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR set. A word-addressing exception may occur.


### Substract Register
* `0x11`
* `SR,R1 R2`
* `OGLE`

The word at the effective address (the subtrahend) is subtracted from the value in register R1 (the minuend) and the difference is stored in R1. The difference is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set. A word-addressing exception may occur.


### Reverse Subtract Register
* `0x12`
* `RSR,R1 R2`
* `OGLE`

This instruction operates the same way as the Subtract Register instruction except that the roles of the minuend and the subtrahend are reversed. 4 4 In all the reversed instructions, although the roles of the two operand values are interchanged, the result is still stored in the same place.


### Multiply Register
* `0x13`
* `MR,R1 R2`
* `OGLE`

The value in register R1 and the word at the effective address are multiplied and the low-order 32 bits of the product are stored in register R1. The result in register R1 is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set. A word-addressing exception may occur.


### Divide Register
* `0x14`
* `DR,R1 R2`
* `OGLE`

The value in register R1 (the dividend) is divided by the word at the effective address (the divisor) and the quotient is stored in register R1. The quotient is selected so that the remainder is nonnegative. The quotient is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set. A word-addressing exception may occur. If the divisor is zero, the zero divisor exception occurs and register R1 is unchanged.


### Reverse Divide Register
* `0x15`
* `RDR,R1 R2`
* `OGLE`

This instruction operates the same way as Divide Register except that the roles of the dividend and divisor are reversed.


### Remainder Register
* `0x16`
* `REMR,R1 R2`
* `GE`

The value in register R1 (the dividend) is divided by the word at the effective address (the divisor) and the nonnegative remainder is stored in register R1. The remainder is compared to zero to set the CCR. A word-addressing exception may occur. If the divisor is zero, the zero divisor exception occur6 and register R1 is unchanged.


### Reverse Remainder Register
* `0x7`
* `RREMR,R1 R2`
* `GE`

This instruction operates the same way as Remainder Register except that the roles of dividend and divisor are reversed.


### Real Add Register
* `0x18`
* `FAR,R1 R2`
* `GLE`

The value in register R1 is added to the real number at the effective address and the sum is stored in register R1. The sum is compared to zero to set the CCR. Both word-addressing and real-format exceptions may occur.


### Real Subtract Register
* `0x19`
* `FSR,R1 R2`
* `GLE`

The real number at the effective address (the subtrahend) is subtracted from the value in the register R1 (the minuend) and the difference is stored in register R1. The difference is compared to zero to set the CCR. Both word-addressing and real format exceptions may occur.


### Reverse Real Subtract Register
* `0x1a`
* `RFSR,R1 R2`
* `GLE`

This instruction is the same as Real Subtract Register with the roles of the minuend and subtrahend reversed.


### Real Multiply Register
* `0x1b`
* `FMR,R1, R2`
* `GLE`

The value in register R1 and the real number at the effective address are multiplied and the product is stored in register R1. The product is compared to zero to set the CCR. Both word-addressing and real format exceptions may occur.


### Real Divide Register
* `0x1c`
* `FDR,R1 R2`
* `GLE`

The value in register R1 (the dividend) is divided by the real number at the effective address (thee divisor) and the quotient is stored in register R1.  The quotient is compared with zero to set the CCR. Word-addressing, real format, and zero divisor exceptions may occur.


### Reverse Real Divide Register
* `0x1d`
* `RFDR,R1 R2`
* `GLE`

This instruction is the same as Real Divide Register with the roles of dividend and divisor reversed.


### Convert To Real Register
* `0x1e`
* `FLOATR,R1 R2`
* `GLE`

The 32-bit two's complement integer at the effective address is converted to a real number and stored in register R1. The real result is compared to zero to set the CCR. A word-addressing exception may occur.


### Convert To Integer Register
* `0x1f`
* `FIXR,R1 R2`
* `OGLE`

The integer portion of the real number at the effective address is converted to a 32-bit two's complement integer and stored in register R1. If overflow occurs, the result is zero and the O bit of the CCR is set. The result is compared to zero to set the other bits of the CCR. A word-addressing exception may occur.

## RS instructions

### Load
* `0x20`
* `L,R1 A,R2`
* `GLE`

This instruction operates in the same way as the Load Register instruction except that the effective address is calculated by using the register- and-storage addressing algorithm.


### Load Negative
* `0x21`
* `LN,R1 A,R2`
* `OGLE`

This instruction operates in the same way as Load Negative Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Store
* `0x22`
* `ST,R1 A,R2`
* `GLE`

This instruction operates in the same way as the Store Register instruction with the effective address calculated by the register-and-storage addressing algorithm.


### Swap
* `0x23`
* `SWAP,R1 A,R2`
* `GLE`

This instruction operates in the same way as the Swap Register instruction with the effective address calculated by the register-and-storage algorithm.


### And
* `0x24`
* `AND,R1 A,R2`
* `GLE`

This instruction operates like the And Register except that the register- and-storage addressing algorithm is used to calculate the effective address.


### Or
* `0x25`
* `OR,R1 A,R2`
* `GLE`

This instruction operates in the same way as And with logical or replacing logical and.


### Exclusive Or
* `0x26`
* `XOR,R1 A,R2`
* `GLE`

This instruction operates in the same way as And with logical and replaced by logical exclusive or.


### Not
* `0x27`
* `NOT,R1 A,R2`
* `GLE`

This instruction operates in the same way as And with logical and replaced by logical complement of the second operand, the original value in register R1 being ignored.


### Branch Conditions Set
* `0x28`
* `BCS,M1 A,R2`
* `None`

This instruction operates in the same way as Branch Conditions Set Register with the effective address calculated by the register-and-storage addressing algorithm.


### Branch Condition Reset
* `0x29`
* `BCR,M1 A,R2`
* `None`

This instruction operates in the same way as Branch Conditions Reset Register with the effective address calculated by the register-and-storage addressing algorithm.


### Branch and Link
* `0x2a`
* `BAL,R1 A,R2`
* `None`

The current contents of the ILC are stored in register R1 and the ILC is loaded with the effective address of the instruction.


### Save Condition
* `0x2b`
* `SAC,M1 A,R2`
* `None`

This instruction operates in the same way as the Store Conditions Register instruction with the effective address calculated by the register- and-storage addressing algorithm.


### Compare
* `0x2c`
* `C,R1 A,R2`
* `GLE`

This instruction operates the same way as Compare Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Supervisor Call
* `0x2e`
* `SVC,R1 A,R2`
* `None`

Program execution is interrupted and a call made to a controlling supervisor program.


### Execute
* `0x2f`
* `EX,R1 A,R2`
* `None`

The instruction at the effective address is executed. The effects of the subject instruction become the effects of the Execute instruction. If the effective address is not even, an execute address exception occurs.  Execute instructions may be nested to any depth. Note that the ILC is changed only if explicitly modified by the subject instruction.


### Load Address
* `0x4e`
* `LA,R1 A,R2`
* `None`

Register R1 is loaded with the instruction's effective address.


### Load Multiple
* `0x6e`
* `LM,R1 A,R2`
* `None`

Registers R1 through R2 are loaded from consecutive words in memory, beginning at the effective address (the effective address is calculated by assuming that the index register designator is zero). If R2 is less than R1, registers R1 through 15 and 0 through R2 are loaded. A word-addressing exception may occur.


### Store Multiple
* `0x6f`
* `STM,R1 A,R2`
* `None`

Registers R1 through R2 are stored into consecutive words of memory, beginning at the effective address (the effective address is calculated by assuming the index register designator is zero). If R2 is less than R1, registers R1 through 15 and 0 through R2 are stored. A word-addressing exception may occur.


### Add RS
* `0x30`
* `A,R1 A,R2`
* `OGLE`

This instruction operates in the same way as Add Register with the effective address calculated by the register-and-storage addressing algorithm.


### Substract
* `0x31`
* `S,R1 A,R2`
* `OGLE`

This instruction operates the same way as Subtract Register with the effective address calculated by the register-and-storage addressing algorithm.


### Reverse Subtract
* `0x32`
* `RS,R1 A,R2`
* `OGLE`

This instruction operates the same way as Subtract except that the roles of the minuend and the subtrahend are reversed.


### Multiply
* `0x33`
* `M,R1 A,R2`
* `OGLE`

This instruction operates the same way as Multiply Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Divide
* `0x34`
* `D,R1 A,R2`
* `OGLE`

This instruction operates the same way as Divide Register except that the effective address is calculated with the register-and-storage addressing algorithm.


### Reverse Divide
* `0x35`
* `RD,R1 A,R2`
* `OGLE`

This instruction operates the same way as Divide except that the roles of the dividend and the divisor are reversed.


### Remainder
* `0x36`
* `REM,R1 A,R2`
* `GE`

This instruction operates the same way as Remainder Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Reverse Remainder
* `0x37`
* `RREM,R1 A,R2`
* `GE`

This instruction operates the same way as Remainder except that the roles of dividend and divisor are reversed.


### Real Add
* `0x38`
* `FA,R1 A,R2`
* `GLE`

This instruction is the same as Real Add Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Real Subtract
* `0x39`
* `FS,R1 A,R2`
* `GLE`

This instruction is the same as Real Subtract Register except that the effective address is calculated by.the register-and-storage addressing algorithm.


### Reverse Real Subtract
* `0x3a`
* `RFS,R1 A,R2`
* `GLE`

This instruction is the same as Real Subtract with the roles of the minuend and subtrahend reversed.


### Real Multiply
* `0x3b`
* `FM,R1 A,R2`
* `GLE`

This instruction is the same as Real Multiply Register except that the effective address is calculated by the register-and-storage addressing routine.


### Real Divide
* `0x3c`
* `FD,R1 A,R2`
* `GLE`

This instruction is the same as Real Divide Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Reverse Real Divide
* `0x3d`
* `RFD,R1 A,R2`
* `GLE`

This instruction is the same as Real Divide with the roles of dividend and divisor reversed.


### Convert To Real
* `0x3e`
* `FLOAT,R1 A,R2`
* `GLE`

This instruction is the same as Convert To Real Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Convert To Integer
* `0x3f`
* `FIX,R1 A,R2`
* `OGLE`

This instruction is the same as Convert To Integer Register except that the effective address is calculated by the register-and-storage addressing algorithm.


### Real Floor
* `0x78`
* `FLOOR,R1 A,R2`
* `GLE`

The real format integer not greater algebraically than the real number at the effective address is stored in register R1. The result is compared to zero to set the CCR. A word-addressing exception can occur.


### Real Ceiling
* `0x79`
* `CEIL,R1 A,R2`
* `GLE`

The real format integer not smaller algebraically than the real number at the effective address is stored in register R1. The result is compared to zero to set the CCR. A word-addressing exception may occur.


### Minimum
* `0x7a`
* `MIN,R1 A,R2`
* `LE`

The values in register R1 and in the word at the effective address are compared and the minimum stored in register R1. The CCR is set by comparing the original register R1 value with the final one. A word-addressing exception may occur.


### Maximum
* `0x7b`
* `MAX,R1 A,R2`
* `GE`

This instruction is the same as Minimum except that the maximum replaces the minimum.


### Shift Logical
* `0x7c`
* `SHIFTL,R1 A,R2`
* `OGLE`

The effective address is treated as a 16-bit two's complement integer called the shift count. The value in register R1 is shifted leftward by the amount of the shift count if positive and rightward if negative, the shift distance measured in bits. Bits shifted off either end of the register are lost.  If a 1 bit is lost, the O bit of the CCR is set. The result is compared to zero to set the other CCR bits. 7 7 A shift count with absolute value greater than 32 causes the same effect as some count with absolute value 32 or less. The smaller count can replace the larger when any shift instruction is executed.


### Shift Circular
* `0x7d`
* `SHIFTC,R1 A,R2`
* `GLE`

This instruction works the same way as Shift Logical except that bits shifted off one end of the register fill vacated positions on the other. Overflow is not possible.


### Shift Arithmetic
* `0x7e`
* `SHIFTA,R1 A,R2`
* `OGLE`

This instruction works like Shift Logical on left shifts and propagates bit 0 rightward on right shifts. Overflow occurs only on left shifts when a bit shifted into the, sign bit differs from one shifted out.


### Shift Real
* `0x7f`
* `SHIFTR,R1 A,R2`
* `GLE`

The effective address is interpreted as a 16-bit two's complement shift count The fraction part of the absolute value of the real number in register R1 is shifted left or right in 4-bit units logically, vacated 4-bit positions being filled with hexadecimal zeros. If the resulting fraction is zero, so is the result. Otherwise the shift count is subtracted from the exponent and the resulting value stored with the original sign in register R1. Overflow cannot occur, but a real format exception may. The result is compared to zero to set the CCR.

## IM instructions

### Load Immediate
* `0x40`
* `LI,R1 I`
* `GLE`

This instruction operates like the Load Register instruction except that the loaded value is the immediate operand I with its sign bit extended left 12 bits. No exceptions can occur.


### Load Negative Immediate
* `0x41`
* `LNI,R1 I`
* `GLE`

The value loaded into register R1 is the 32-bit two's complement of the 20-bit two's complement value I. Overflow cannot occur. The CCR is set by comparing the loaded value with zero.


### And Immediate
* `0x44`
* `ANDI,R1 I`
* `LE`

The logical and of the word in register R1 and the 20-bit immediate value I extended on the left with 12 zero bits is stored in R1. The CCR is set in the same way as the And Register instruction.


### Or Immediate
* `0x45`
* `ORI,R1 I`
* `GLE`

This instruction operates in the same way as And Immediate with logical and replaced by logical or.


### Exclusive Or Immediate
* `0x46`
* `XORI,R1 I`
* `GLE`

This instruction operates in the same way as And Immediate with logical and replaced by logical exclusive or.


### Not Immediate
* `0x47`
* `NOTI,R1 I`
* `GLE`

This instruction operates in the same way as And Immediate with logical and replaced by logical complement of the extended immediate value, the original value in register R1 being ignored.


### Compare Immediate
* `0x4c`
* `CI,R1, I`
* `GLE`

The 32-bit value in register R1 is compared algebraically with the 32-bit value constructed by propagating the immediate operand's sign bit leftward 12 bits, and the result is used to set the G, L, or E bit of the CCR as appropriate.


### Add Immediate
* `0x50`
* `AI,R1 I`
* `OGLE`

The 20-bit two's complement immediate operand I is added to the value in register R1 and the sum stored in R1. The sum is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set.


### Substract Immediate
* `0x51`
* `SI,R1 I`
* `OGLE`

The 20-bit two's complement integer immediate operand I (the subtrahend) is subtracted from the value in register R1 (the minuend) and the result stored in register R1. The difference is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set.


### Reverse Subtract Immediate
* `0x52`
* `RSI,R1 I`
* `OGLE`

This instruction operates the same way as Subtract Immediate except that the roles of the minuend and the subtrahend are reversed.


### Multiply Immediate
* `0x53`
* `MI,R1 I`
* `OGLE`

The low 32 bits of the product of the value in register R1 and the 20-bit immediate value I are stored in register R1. The product in register R1 is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set.


### Divide Immediate
* `0x54`
* `DI,R1 I`
* `OGLE`

The value in register R1 (the dividend) is divided by the 20-bit two's complement integer immediate value I (the divisor) and the quotient is stored in register R1. The quotient is selected so that the remainder is nonnegative. The quotient is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set. If the divisor is zero, the zero divisor exception occurs and the register R1 is unchanged.


### Reverse Divide Immediate
* `0x55`
* `RDI,R1 I`
* `GLE`

This instruction operates the same way as Divide Immediate except that the roles of the dividend and the divisor are reversed. Overflow is not possible.


### Remainder Immediate
* `0x56`
* `REMI,R1 I`
* `GE`

The value in register R1 (the dividend) is divided by the 20-bit two's complement value I (the divisor) and the nonnegative remainder is stored in register R1. The remainder is compared to zero to set the CCR. If the divisor is zero, the zero divisor exception occurs and register R1 is unchanged.


### Reverse Remainder Immediate
* `0x57`
* `RREMI,R1 I`
* `GE`

This instruction is the same as Remainder Immediate except that the roles of dividend and divisor are reversed.


### Real Add Immediate
* `0x58`
* `FAI,R1 I`
* `GLE`

The sum of the value in register R1 and the real short format immediate operand I is stored in register R1. A real format exception may occur.


### Real Subtract Immediate
* `0x59`
* `FSI,RI I`
* `GLE`

The short format real imm_diate operand I (the subtrahend) is subtracted from the value in register R1 (the minuend) and the difference is stored in register R1. The difference is compared to zero to set the CCR. A real-format exception can occur.


### Reverse Real Subtract Immediate
* `0x5a`
* `RFSI,R1 I`
* `GLE`

This instruction is the same as Real Subtract Immediate with the roles of the minuend and the subtrahend reversed.


### Real Multiply Immediate
* `0x5b`
* `FMI,R1 I`
* `GLE`

The value in register R1 is multiplied by the real short format immediate value I and the product is stored in register R1. The product is compared to zero to set the CCR. A real format exception may occur.


### Real Divide Immediate
* `0x5c`
* `FD1,R1 I`
* `GLE`

The value in register R1 (the dividend) is divided by the real short format immediate value I (the divisor) and the result stored in register R1. The quotient is compared to zero to set the CCR. Both real format and zero divisor exceptions may occur.


### Reverse Real Divide Immediate
* `0x5d`
* `RFDI,R1 I`
* `GLE`

This instruction is the same as Real Divide Immediate with the roles of dividend and divisor reversed.


### Convert To Real Immediate
* `0x5e`
* `FLOATI,R1 I`
* `GLE`

The 20-bit two's complement integer immediate operand I is converted to real format and stored in register R1. The result is compared to zero to set the CCR.


### Convert to Integer Immediate
* `0x5f`
* `FIXI,R1 I`
* `OGLE`

The real short format immediate operand I is converted to a 32-bit two's complement integer and the result stored in register R1. If overflow occurs, the result is zero and the O bit of the CCR is set. The result is compared to zero to set the other CCR bits.

## CH instructions

### Load Character
* `0x60`
* `LC,R1 A,R2`
* `GE`

Register R1 is cleared to zero, and the character at the effective address is loaded into bits 24 through 31. The loaded value is compared to zero and either the G or E bit of the CCR set.


### Load Negative Character
* `0x61`
* `LNC,R1 A,R2`
* `LE`

The character at the effective address is extended leftward 24 bits with zeros and the resulting word complemented and loaded into register R1.  Overflow cannot occur. The loaded value is compared with zero to set the CCR.


### Store Character
* `0x62`
* `STC,R1 A,R2`
* `GE`

Bits 24 through 31 are stored in the character at the effective address. The stored value is compared to zero to set the CCR.


### Swap Character
* `0x63`
* `SWAPC,R1 A,R2`
* `GE`

Bits 24 through 31 are exchanged with the character at the effective address. The CCR is set by comparing the character loaded into the register with zero. Bits 0 through 23 of register R1 are not affected.


### And Character
* `0x64`
* `ANDC,R1 A,R2`
* `GLE`

The character at the effective address is anded with bits 24 through 31 of register R1 and the result is replaced in bits 24 through 31 of R1. Bits 0 through 23 of R1 are not affected. The CCR is set in the same way as the And Register instruction.


### Or Character
* `0x65`
* `ORC,R1 A,R2`
* `GLE`

This instruction operates in the same way as And Character with logical and replaced by logical or.


### Exclusive Or Character
* `0x66`
* `XORC,R1 A,R2`
* `GLE`

This instruction operates in the same as And Character with logical and replaced by logical exclusive or.


### Not Character
* `0x67`
* `NOTC,R1 A,R2`
* `GLE`

This instruction operates in the same way as And Character with logical and replaced by logical complement of the second operand, the original value of bits 24 through 31 of register R1 being ignored.


### Save Condition Character
* `0x6b`
* `SACC,M1 A,R2`
* `None`

If the logical and of the CCR and the 4 bit mask field M1 is nonzero, a character of all one bits is stored at the effective address; otherwise a character of all zero bits is stored.


### Compare Character
* `0x6c`
* `CC,R1 A,R2`
* `GLE`

Bits 24 through 31 of register R1 are compared as an 8-bit positive integer with the character at the effective address, and the result is used to set the G, L, or E bit of the CCR as appropriate.


### Add Character
* `0x70`
* `AC,R1 A,R2`
* `OGLE`

The character at the effective address is extended 24 bits to the left with zeros and added to the value in register R1 with the result loaded into R1.  The sum is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set.


### Subtract Character
* `0x71`
* `SC,R1 A,R2`
* `OGLE`

The character at the effective address (the subtrahend), treated as a positive integer by extension 24 bits leftward with zeros, is subtracted from the value in register R1 (the minuend) and the result stored in R1. The difference is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set.


### Reverse Subtract Character
* `0x72`
* `RSC,R1 A,R2`
* `OGLE`

This instruction operates the same way as the Subtract Character with the roles of the minuend and the subtrahend reversed.


### Multiply Character
* `0x73`
* `MC,R1 A,R2`
* `OGLE`

The low 32 bits of the product of the value in register R1 and the positive 8-bit integer in the character at the effective address are stored in register R1. The value in register R1 is compared to zero to set the CCR. If overflow occurs, only the O bit of the CCR is set.


### Divide Character
* `0x74`
* `DC,R1 A,R2`
* `GLE`

The value in register R1 (the dividend) is divided by the positive 8-bit integer at the effective address (the divisor) and the quotient is stored in register R1. The quotient is selected so that the remainder is nonnegative.  The quotient is compared to zero to set the CCR. If the divisor is zero, the zero divisor exception occurs and register R1 is unchanged. Overflow is not possible.


### Reverse Divide Character
* `0x75`
* `RDC,R1 A,R2`
* `GLE`

This instruction operates the same way as Divide Character except that the roles of the dividend and the divisor are reversed.


### Remainder Character
* `0x76`
* `REMC,R1 A,R2`
* `GE`

The value in register R1 (the dividend) is divided by the 8-bit positive integer (the divisor) at the effective address and the nonnegative remainder is stored in register R1. The remainder is compared to zero to set the CCR. If the divisor is zero, the zero divisor exception occurs and register R1 is unchanged.


### Reverse Remainder Character
* `0x77`
* `RREMC,R1 A,R2`
* `GE`

This instruction is the same as Remainder Character except that the roles of dividend and divisor are reversed.
