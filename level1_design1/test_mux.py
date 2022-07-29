# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #test for 12th input
    input12=0b00
    input13=0b10
    select=0b01100 #12th line

    #input driving
    dut.inp12.value=input12
    dut.inp13.value=input13
    dut.sel.value=select

    await Timer(2, units='ns')

    #cocotb.log.info(f'input12={input12:0b00} select={select:0b01100} DUT:{dut.out.value:0b00}')
    assert dut.out.value == 0b00, f"Mux output is incorrect: {dut.X.value} != 0b00"
