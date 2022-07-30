# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #test for 12th input
    input12=0b00
    input13=0b11
    select=0b01101 #13th line

    #input driving
    dut.inp12.value=input12
    dut.inp13.value=input13
    dut.sel.value=select

    await Timer(2, units='ns')

    #cocotb.log.info(f'input12={input12:0b00} select={select:0b01101} model={input13:0b11} DUT:{dut.out.value:0b00}')
    assert dut.out.value == 0b11, f"Mux output is incorrect: {dut.out.value} != 0b11"

@cocotb.test()
async def test2_mux(dut):
    """Test for mux2"""
    #test for 30th input
    input30=0b00
    select=0b11111 #30th line

    #input driving
    dut.inp30.value=input30
    dut.sel.value=select

    await Timer(2, units='ns')

    #cocotb.log.info(f'input12={input12:0b00} select={select:0b01101} model={input13:0b11} DUT:{dut.out.value:0b00}')
    assert dut.out.value == 0b00, f"Mux output is incorrect: {dut.out.value} != 0b00"