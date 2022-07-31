# CTB Hackathon 2022 - Arpit Sharma Report
▫️ The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.  
▫️ Gitpod screenshot 👇

![ss](https://user-images.githubusercontent.com/68592620/182046281-7a83b469-d9e3-48ce-86e9-59fcb49111a8.png)  
## Level 1 - Design 1  
**Multiplexer**  
In this given design we have a 31:1 multiplexer with 5 select lines. Each input & output line is two bit bus signal.  
The assert statement is used to check whether the observed outut is same as the expected output or not.  
The following errors are seen.

![bugs_mux](https://user-images.githubusercontent.com/68592620/182046801-56142189-f087-4744-9271-9bc77367fc8d.png)  

**Test Scenario 1**  
- Test Inputs: inp12= 0b00, inp13=0b11, sel=0b01101
- Expected Output: out= 0b11
- Observed Output in the DUT is not equal to 0b11.  
  Since the observed output is not equal to the expected output therefore the given design has bugs.
