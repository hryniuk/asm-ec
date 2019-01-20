# Instructions
| name | opcode | syntax | poss. condition bits affected|
|------|--------|--------|----------------|
| Load Register | `0x0` | `LR,R1 R2` | `GLE` |
| Load Negative Register | `0x1` | `LNR,R1 R2` | `OGLE` |
| Store Register | `0x2` | `STR,R1 R2` | `GLE` |
| Swap Register | `0x3` | `SWAPR,R1 R2` | `GLE` |
| And Register | `0x4` | `ANDR,R1 R2` | `GLE` |
| Or Register | `0x5` | `ORR,R1 R2` | `GLE` |
| Exclusive Or Register | `0x6` | `XORR,R1 R2` | `GLE` |
| Not Register | `0x7` | `NOTR,R1 R2` | `GLE` |
| Branch Conditions Set Register | `0x8` | `BCSR,M1 R2` | `None` |
| Branch Conditions Reset Register | `0x9` | `BCRR,M1 R2` | `None` |
| Branch and Link Register | `0xa` | `BALR,R1 R2` | `None` |
| Save Condition Register | `0xb` | `SACR,M1 R2` | `None` |
| Compare Register | `0xc` | `CR,R1 R2` | `GLE` |
| Compare Character String | `0xe` | `CCS,M1 R2` | `GLE` |
| Move Character String | `0xf` | `MCS,M1 R2` | `None` |
| Add Register | `0x10` | `AR,R1 R2` | `OGLE` |
| Substract Register | `0x11` | `SR,R1 R2` | `OGLE` |
| Reverse Subtract Register | `0x12` | `RSR,R1 R2` | `OGLE` |
| Multiply Register | `0x13` | `MR,R1 R2` | `OGLE` |
| Divide Register | `0x14` | `DR,R1 R2` | `OGLE` |
| Reverse Divide Register | `0x15` | `RDR,R1 R2` | `OGLE` |
| Remainder Register | `0x16` | `REMR,R1 R2` | `GE` |
| Reverse Remainder Register | `0x7` | `RREMR,R1 R2` | `GE` |
| Real Add Register | `0x18` | `FAR,R1 R2` | `GLE` |
| Real Subtract Register | `0x19` | `FSR,R1 R2` | `GLE` |
| Reverse Real Subtract Register | `0x1a` | `RFSR,R1 R2` | `GLE` |
| Real Multiply Register | `0x1b` | `FMR,R1, R2` | `GLE` |
| Real Divide Register | `0x1c` | `FDR,R1 R2` | `GLE` |
| Reverse Real Divide Register | `0x1d` | `RFDR,R1 R2` | `GLE` |
| Convert To Real Register | `0x1e` | `FLOATR,R1 R2` | `GLE` |
| Convert To Integer Register | `0x1f` | `FIXR,R1 R2` | `OGLE` |
| Load | `0x20` | `L,R1 A,R2` | `GLE` |
| Load Negative | `0x21` | `LN,R1 A,R2` | `OGLE` |
| Store | `0x22` | `ST,R1 A,R2` | `GLE` |
| Swap | `0x23` | `SWAP,R1 A,R2` | `GLE` |
| And | `0x24` | `AND,R1 A,R2` | `GLE` |
| Or | `0x25` | `OR,R1 A,R2` | `GLE` |
| Exclusive Or | `0x26` | `XOR,R1 A,R2` | `GLE` |
| Not | `0x27` | `NOT,R1 A,R2` | `GLE` |
| Branch Conditions Set | `0x28` | `BCS,M1 A,R2` | `None` |
| Branch Condition Reset | `0x29` | `BCR,M1 A,R2` | `None` |
| Branch and Link | `0x2a` | `BAL,R1 A,R2` | `None` |
| Save Condition | `0x2b` | `SAC,M1 A,R2` | `None` |
| Compare | `0x2c` | `C,R1 A,R2` | `GLE` |
| Supervisor Call | `0x2e` | `SVC,R1 A,R2` | `None` |
| Execute | `0x2f` | `EX,R1 A,R2` | `None` |
| Load Address | `0x4e` | `LA,R1 A,R2` | `None` |
| Load Multiple | `0x6e` | `LM,R1 A,R2` | `None` |
| Store Multiple | `0x6f` | `STM,R1 A,R2` | `None` |
| Add RS | `0x30` | `A,R1 A,R2` | `OGLE` |
| Substract | `0x31` | `S,R1 A,R2` | `OGLE` |
| Reverse Subtract | `0x32` | `RS,R1 A,R2` | `OGLE` |
| Multiply | `0x33` | `M,R1 A,R2` | `OGLE` |
| Divide | `0x34` | `D,R1 A,R2` | `OGLE` |
| Reverse Divide | `0x35` | `RD,R1 A,R2` | `OGLE` |
| Remainder | `0x36` | `REM,R1 A,R2` | `GE` |
| Reverse Remainder | `0x37` | `RREM,R1 A,R2` | `GE` |
| Real Add | `0x38` | `FA,R1 A,R2` | `GLE` |
| Real Subtract | `0x39` | `FS,R1 A,R2` | `GLE` |
| Reverse Real Subtract | `0x3a` | `RFS,R1 A,R2` | `GLE` |
| Real Multiply | `0x3b` | `FM,R1 A,R2` | `GLE` |
| Real Divide | `0x3c` | `FD,R1 A,R2` | `GLE` |
| Reverse Real Divide | `0x3d` | `RFD,R1 A,R2` | `GLE` |
| Convert To Real | `0x3e` | `FLOAT,R1 A,R2` | `GLE` |
| Convert To Integer | `0x3f` | `FIX,R1 A,R2` | `OGLE` |
| Real Floor | `0x78` | `FLOOR,R1 A,R2` | `GLE` |
| Real Ceiling | `0x79` | `CEIL,R1 A,R2` | `GLE` |
| Minimum | `0x7a` | `MIN,R1 A,R2` | `LE` |
| Maximum | `0x7b` | `MAX,R1 A,R2` | `GE` |
| Shift Logical | `0x7c` | `SHIFTL,R1 A,R2` | `OGLE` |
| Shift Circular | `0x7d` | `SHIFTC,R1 A,R2` | `GLE` |
| Shift Arithmetic | `0x7e` | `SHIFTA,R1 A,R2` | `OGLE` |
| Shift Real | `0x7f` | `SHIFTR,R1 A,R2` | `GLE` |
| Load Immediate | `0x40` | `LI,R1 I` | `GLE` |
| Load Negative Immediate | `0x41` | `LNI,R1 I` | `GLE` |
| And Immediate | `0x44` | `ANDI,R1 I` | `LE` |
| Or Immediate | `0x45` | `ORI,R1 I` | `GLE` |
| Exclusive Or Immediate | `0x46` | `XORI,R1 I` | `GLE` |
| Not Immediate | `0x47` | `NOTI,R1 I` | `GLE` |
| Compare Immediate | `0x4c` | `CI,R1, I` | `GLE` |
| Add Immediate | `0x50` | `AI,R1 I` | `OGLE` |
| Substract Immediate | `0x51` | `SI,R1 I` | `OGLE` |
| Reverse Subtract Immediate | `0x52` | `RSI,R1 I` | `OGLE` |
| Multiply Immediate | `0x53` | `MI,R1 I` | `OGLE` |
| Divide Immediate | `0x54` | `DI,R1 I` | `OGLE` |
| Reverse Divide Immediate | `0x55` | `RDI,R1 I` | `GLE` |
| Remainder Immediate | `0x56` | `REMI,R1 I` | `GE` |
| Reverse Remainder Immediate | `0x57` | `RREMI,R1 I` | `GE` |
| Real Add Immediate | `0x58` | `FAI,R1 I` | `GLE` |
| Real Subtract Immediate | `0x59` | `FSI,RI I` | `GLE` |
| Reverse Real Subtract Immediate | `0x5a` | `RFSI,R1 I` | `GLE` |
| Real Multiply Immediate | `0x5b` | `FMI,R1 I` | `GLE` |
| Real Divide Immediate | `0x5c` | `FD1,R1 I` | `GLE` |
| Reverse Real Divide Immediate | `0x5d` | `RFDI,R1 I` | `GLE` |
| Convert To Real Immediate | `0x5e` | `FLOATI,R1 I` | `GLE` |
| Convert to Integer Immediate | `0x5f` | `FIXI,R1 I` | `OGLE` |
| Load Character | `0x60` | `LC,R1 A,R2` | `GE` |
| Load Negative Character | `0x61` | `LNC,R1 A,R2` | `LE` |
| Store Character | `0x62` | `STC,R1 A,R2` | `GE` |
| Swap Character | `0x63` | `SWAPC,R1 A,R2` | `GE` |
| And Character | `0x64` | `ANDC,R1 A,R2` | `GLE` |
| Or Character | `0x65` | `ORC,R1 A,R2` | `GLE` |
| Exclusive Or Character | `0x66` | `XORC,R1 A,R2` | `GLE` |
| Not Character | `0x67` | `NOTC,R1 A,R2` | `GLE` |
| Save Condition Character | `0x6b` | `SACC,M1 A,R2` | `None` |
| Compare Character | `0x6c` | `CC,R1 A,R2` | `GLE` |
| Add Character | `0x70` | `AC,R1 A,R2` | `OGLE` |
| Subtract Character | `0x71` | `SC,R1 A,R2` | `OGLE` |
| Reverse Subtract Character | `0x72` | `RSC,R1 A,R2` | `OGLE` |
| Multiply Character | `0x73` | `MC,R1 A,R2` | `OGLE` |
| Divide Character | `0x74` | `DC,R1 A,R2` | `GLE` |
| Reverse Divide Character | `0x75` | `RDC,R1 A,R2` | `GLE` |
| Remainder Character | `0x76` | `REMC,R1 A,R2` | `GE` |
| Reverse Remainder Character | `0x77` | `RREMC,R1 A,R2` | `GE` |
