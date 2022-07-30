# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    input=0b1
    dut.inp_bit.value=input          #input driving
    #await Timer(12, units='us')
    assert dut.seq_seen.value == 0b0, f"seq_seenput is incorrect: {dut.seq_seen.value} != 0b0"
    
    input=0b1
    dut.inp_bit.value=input          #input driving
    #await Timer(12, units='us')
    assert dut.seq_seen.value == 0b0, f"seq_seenput is incorrect: {dut.seq_seen.value} != 0b0"
       
    input=0b0
    dut.inp_bit.value=input          #input driving
    #await Timer(12, units='us')
    assert dut.seq_seen.value == 0b0, f"seq_seenput is incorrect: {dut.seq_seen.value} != 0b0"

    input=0b1
    dut.inp_bit.value=input          #input driving
    #await Timer(12, units='us')
    assert dut.seq_seen.value == 0b0, f"seq_seenput is incorrect: {dut.seq_seen.value} != 0b0"

    input=0b1
    dut.inp_bit.value=input          #input driving
    #await Timer(12, units='us')
    assert dut.seq_seen.value == 0b1, f"seq_seenput is incorrect: {dut.seq_seen.value} != 0b1"

    #cocotb.log.info('#### CTB: Develop your test here! ######')
