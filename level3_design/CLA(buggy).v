//this code is written by me, with the resources available in the NPTEL course of System design through VERILOG.
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
         p[2]=a[2]~^b[2], //bug added to this line
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
