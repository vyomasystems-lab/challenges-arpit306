import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_cla(dut):
    """Test for cla"""
    A=0b0101
    B=0b0010
    Carryin=0b0

    #input driving
    dut.a.value=A
    dut.b.value=B
    dut.cin.value=Carryin

    await Timer(2, units='ns')

    assert dut.sum.value == 0b0111, f"output is incorrect: {dut.sum.value} != 0b0111"
