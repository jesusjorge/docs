### Test

We will be using CUInt128<br/>
which mean that the max value we can get in one single byte is 250<br/>
Total test: `74 byte(s)` sequence, `21` tests

| ULong | Encoding |
| ------| -------- |
| 21 | `15` |
| null | `ff` |
| 0 | `00` |
| 1 | `01` |
| 2 | `02` |
| 3 | `03` |
| 249 | `f9` |
| 250 | `fa` (max single byte value for CUInt128) |
| 251 | `fe` `00` `fb` |
| 253 | `fe` `00` `fd` |
| 254 | `fe` `00` `fe` |
| 255 | `fe` `00` `ff` |
| 256 | `fe` `01` `00` |
| 257 | `fe` `01` `01` |
| 16777214 | `fd` `00` `ff` `ff` `fe` |
| 16777215 | `fd` `00` `ff` `ff` `ff` |
| 16777216 | `fd` `01` `00` `00` `00` |
| 16777217 | `fd` `01` `00` `00` `01` |
| 4294967294 | `fd` `ff` `ff` `ff` `fe` |
| 4294967295 | `fd` `ff` `ff` `ff` `ff` |
| 4294967296 | `fc` `00` `00` `00` `01` `00` `00` `00` `00` |
| 4294967297 | `fc` `00` `00` `00` `01` `00` `00` `00` `01` |

[Definition](https://github.com/jesusjorge/s13n/wiki/1.1)
