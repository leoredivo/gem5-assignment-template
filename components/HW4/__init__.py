# Copyright (c) 2024 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.memory.dram_interfaces.ddr4 import DDR4_2400_8x8
from gem5.components.memory.memory import ChanneledMemory
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA

from cache_hierarchies import HW4SmallCache, HW4MediumCache, HW4LargeCache

HW4RISCVBoard = SimpleBoard


class HW4DDR4(ChanneledMemory):
    """
    HW4DDR4 models a 1 GiB single channel DDR4 DRAM memory with a data
    bus clocked at 2400MHz.
    """

    def __init__(self):
        super().__init__(DDR4_2400_8x8, 1, 128, size="1GiB")


class HW4O3CPU(SimpleProcessor):
    """
    HW4O3CPU implements a single core out of order processor for the RISC-V ISA
    Parameters are the O3CPU defaults.
    """

    def __init__(self):
        super().__init__(cpu_type=CPUTypes.O3, num_cores=1, isa=ISA.RISCV)


__all__ = [
    "HW4RISCVBoard",
    "HW4DDR4",
    "HW4O3CPU",
    "HW4SmallCache",
    "HW4MediumCache",
    "HW4LargeCache",
]