# CTB Hackathon 2022 - Arpit Sharma Report
▫️ The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.  
▫️ Gitpod screenshot 👇

![ss](https://user-images.githubusercontent.com/68592620/182046281-7a83b469-d9e3-48ce-86e9-59fcb49111a8.png)  
## Level 1 - Design 1  
**Multiplexer**  
In this given design we have a 31:1 multiplexer with 5 select lines. Each input & output line is two bit bus signal.  
The values are assigned to input port using
```
dut.inp12.value=0b00
dut.inp13.value=0b11
dut.sel.value=0b01101
```
The assert statement is used to check whether the observed outut is same as the expected output or not.  
The following error is seen.
![bugs_mux](https://user-images.githubusercontent.com/68592620/182046801-56142189-f087-4744-9271-9bc77367fc8d.png)

