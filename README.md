# CTB Hackathon 2022 - Final Report  

This is the final hackathon report by Arpit Sharma, submitted for evaluation.

## Table of contents  
▫️[Abstract](https://github.com/vyomasystems-lab/challenges-arpit306/edit/master/README.md#abstract)  
▫️[Level-1_Design-1](https://github.com/vyomasystems-lab/challenges-arpit306/edit/master/README.md#abstract)  
▫️[Level-1_Design-2](https://github.com/vyomasystems-lab/challenges-arpit306/edit/master/README.md#abstract)  
▫️[Level-2_Design](https://github.com/vyomasystems-lab/challenges-arpit306/edit/master/README.md#abstract)  
▫️[Level-3_Design](https://github.com/vyomasystems-lab/challenges-arpit306/edit/master/README.md#abstract)
## Abstract  

▫️ This readme file presents the final report for the Capture The Bug CTB Design Verification Hackathon 2020.  
▫️ The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.  
▫️ Gitpod screenshot 👇

![ss](https://user-images.githubusercontent.com/68592620/182046281-7a83b469-d9e3-48ce-86e9-59fcb49111a8.png)  
## Level 1 - Design 1  
**Multiplexer**  
In this given design we have a 31:1 multiplexer with 5 select lines. Each input & output lines are all a two bit bus signal.
The assert statement is used to check whether the observed output is same as the expected output or not.  
The following errors 👇 were seen.

![bugs_mux](https://user-images.githubusercontent.com/68592620/182046801-56142189-f087-4744-9271-9bc77367fc8d.png)  

**Test Scenario 1**  
- Test Inputs: inp12= 0b00, inp13=0b11, sel=0b01101
- Expected Output: out= 0b11
- Observed Output in the DUT = 0 (default case value ) is not equal to 0b11.  
  Since the observed output is not equal to the expected output therefore the given design has bug.
  
**BUG 1**
```
5'b01011: out = inp11;   
5'b01101: out = inp12;  => bug [ for 12th input line, select value corresponding to 13th input is selected ]
5'b01101: out = inp13;
 default: out = 0;
```
  To fix the bug replace ```5'b01101: out = inp12;``` with ```5'b01100: out = inp12;```  
 
**Test Scenario 2**  
- Test Inputs: inp30=0b01, sel=0b11110
- Expected Output: out= 0b01
- Observed Output in the DUT = 0 (default case value ) is not equal to 0b01.  
  Since the observed output is not equal to the expected output therefore the given design has bug.
  
**BUG 2**
```
5'b11101: out = inp29; 
 default: out = 0;      => bug [ 30th input not included in case statement ]
```
  To fix the bug we insert a line of ```5'b11110: out = inp30;``` before ```default: out = 0;```

**DESIGN FIX**
```
# corrected code
module mux(sel,inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, 
           inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17,
           inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,
           inp27, inp28, inp29, inp30, out);

  input [4:0] sel;
  input [1:0] inp0, inp1, inp2, inp3, inp4, inp5, inp6,
            inp7, inp8, inp9, inp10, inp11, inp12, inp13, 
            inp14, inp15, inp16, inp17, inp18, inp19, inp20,
            inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30;

  output [1:0] out;
  reg [1:0] out;

  // Based on sel signal value, one of the inp0-inp30 gets assigned to the 
  // output signal
  always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 )

  begin
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01100: out = inp12;   // Bug 1 fix
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;   // Bug 2 fix
      default: out = 0;
    endcase
  end

endmodule 
``` 
## Level 1 Design 2
**1011 Overlapping Sequence Detector**  
In this design an overlapping 1011 sequence detector was modelled as an FSM. The modelling style used in the design is an example of Moore FSM, as the output is determined by the current state only. The assert statement is used to check whether the observed output is same as the expected output or not.
The following errors 👇 were seen.

![bugs_1011](https://user-images.githubusercontent.com/68592620/182128763-280e332f-ba3d-46d2-a5f5-6a940aacc0e7.png)

**Test Scenario 1**  
- Test Inputs: input sequence = 0b11011
- Expected Output: sequence seen = 0b00001
- Observed Output in the DUT is = 0b00000
  Since the observed output is not equal to the expected output therefore the given design has bug.
  
**BUG 1**  
```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE; => bug [ next state should be SEQ_1, in order to detect overlapping sequence ]
        else
          next_state = SEQ_10;
      end
```
To fix the bug replace ```next_state = IDLE;``` with ```next_state = SEQ_1;```

**Test Scenario 2**  
- Test Inputs: input sequence = 0b101011
- Expected Output: sequence seen = 0b00001
- Observed Output in the DUT is = 0b00000
  Since the observed output is not equal to the expected output therefore the given design has bug.  
  
**BUG 2**  
```
 SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;    => bug [ next state should be SEQ_10, in order to detect overlapping sequence ]
      end
```
To fix the bug replace ```next_state = IDLE;``` with ```next_state = SEQ_10;```  

**Test Scenario 3**  
- Test Inputs: input sequence = 0b1011011
- Expected Output: sequence seen = 0b0001001
- Observed Output in the DUT is = 0b00010000
  Since the observed output is not equal to the expected output therefore the given design has bug.  
  
**Test Scenario 4**  
- Test Inputs: input sequence = 0b10111011
- Expected Output: sequence seen = 0b00010001
- Observed Output in the DUT is = 0b00010000
  Since the observed output is not equal to the expected output therefore the given design has bug.  
  
**BUG 3 & 4**  
```
   SEQ_1011:
      begin
        next_state = IDLE;    => bug [ in order to detect overlapping sequence, the next state shoud be determined according to the input bits (0 or 1) ]
      end
```
To fix the bug replace 
```  
    SEQ_1011:
      begin
        next_state = IDLE;
      end
``` 
with 

```
 SEQ_1011:
      begin
        if(inp_bit==1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
```
**DESIGN FIX**  
This design has bugs due to incorrect next state assignments, in order to detect overlapping 1011 sequences. The correct state transition diagram for a 1011 overlapping sequence detector should be as follows 👇.  

![FSM](https://user-images.githubusercontent.com/68592620/182138856-a808139b-8196-4874-b837-707cd0d20f7e.jpg)

```
# corrected code
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;     // Bug 1 fixed
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;      // Bug 2 fixed
      end
      SEQ_1011:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;       // Bug 4 fixed
        else
          next_state = SEQ_10;      // Bug 3 fixed
      end
    endcase
  end
endmodule
```

## Level 2 Design  
This design is a complex Bit Manipulation Co-Processor used in a complex microprocessor. This is basically a 32 bit ALU, that takes three 32 bit operands and takes a 32 bit instruction, according to which it generates a 33 bit output, out of which the LSB is the validity bit & the other 32 bits are the output of the operation defined by the instruction. Here we were given the Instruction table, using which the instruction code can be generated to run test cases. Shown below 👇.  

![ISR](https://user-images.githubusercontent.com/68592620/182141607-ba0ac425-7063-48fc-a9c6-aceb057fa38c.png)

**TEST SCENARIO**  
There are 27 * unmarked instructions in the table above. I converted all those instructions to their correponding hex-codes, assuming all the unspecified bits like rs2, rs3 etc... as 0. And ran tests for all those 27 instructions with the inputs shown below 👇  
```    
       # Test case 1
       mav_putvalue_src1 = 0x7FFFFFFF                         
       mav_putvalue_src2 = 0x00000000                                
       mav_putvalue_src3 = 0x0446FF8B                                
       mav_putvalue_instr = (all 27 instructions one by one)   
        
       # Test case 2
       mav_putvalue_src1 = (random 32 bit binary number)  
       mav_putvalue_src2 = (random 32 bit binary number)  
       mav_putvalue_src3 = 0x0446FF8B  
       mav_putvalue_instr = (all 27 instructions one by one)      
```       

**DESIGN BUG**  
After running tests for 27 different instrutions, for two different set of inputs, only one assertion test failure was observed as shown below 👇  

![bugs_alu](https://user-images.githubusercontent.com/68592620/182166406-bcad250b-5d89-4cda-8821-4ec8734c6533.png)

**DESIGN FIX**  
According tp the test reports, the code related to the instruction code **0x40007033** which corresponds to the instruction **ANDN contains the bug.** And it should be corrected by the designer, with the knowledge of the design.

## Level 3 Design  
This design, which I have chosen is the design of a 5-Bit Carry Look-Ahead (CLA) Adder. Refer the Literature Survey Report for more information about the design. I have inserted bug in this design, mentioned below.  

**INSERTED BUG**  
```
module CLA(cout,sum,a,b,cin);

  output cout;
  output [3:0]sum;
  input cin;
  input [3:0]a,b;
  wire [4:1]c;
  wire [3:0]p,g;
  //stage 1 : (p & g generator)
  assign p[0]=a[0]^b[0],
         p[1]=a[1]^b[1],
         p[2]=a[2]~^b[2],  //bug added to this line [ xnor operator instead of xor operator ]
         p[3]=a[3]^b[3];

  assign g[0]=a[0]&b[0],
         g[1]=a[1]&b[1],
         g[2]=a[2]&b[2],
         g[3]=a[3]&b[3];
  //stage2 : CGN
  assign c[1]=g[0]|(p[0]&cin),
         c[2]=g[1]|(p[1]&g[0])|(p[1]&p[0]&cin),
         c[3]=g[2]|(p[2]&g[1])|(p[2]&p[1]&g[0])|(p[2]&p[1]&p[0]&cin),
         cout=g[3]|(p[3]&g[2])|(p[3]&p[2]&g[1])|(p[3]&p[2]&p[1]&g[0])|(p[3]&p[2]&p[1]&p[0]&cin);
  //stage3 : Sum generator
  assign sum[0]=p[0]^cin,
         sum[1]=p[1]^c[1],
         sum[2]=p[2]^c[2],
         sum[3]=p[3]^c[3];
endmodule
```
**TEST SCENARIO**  
In the code above, you can observe where the bug is inserted. The bug is inserted by replacing the xor operator with xnor operator as shown.  
```p[2]=a[2]~^b[2], // ~^ instead of ^ ```  
 ```
    # Test case inputs
    A=0b0101  
    B=0b0010  
    Carryin=0b0  
```

**TEST RESULTS**  
The assert statement is used to check whether the observed output is same as the expected output or not.  
```
assert dut.sum.value == 0b0111, f"output is incorrect: {dut.sum.value} != 0b0111"  
```
The following error 👇 was seen.  

![bugs_CLA](https://user-images.githubusercontent.com/68592620/182179565-88abadfd-4519-4fea-9a78-00beef2af628.png)
