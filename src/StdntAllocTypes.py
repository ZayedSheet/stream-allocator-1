## @file StdntAllocTypes.py
#  @author Zayed Sheet
#  @brief This module is to represent certain data as Enum or NamedTuple
#  @date 2019-02-11


from enum import Enum
from typing import NamedTuple
from SeqADT import *


## @brief class for GenT datatype
#  @details Enumerated datatype for gender
class GenT(Enum):
    male = 'male'
    female = 'female'


## @brief class for DeptT datatype
#  @details Enumerated datatype for departments
class DeptT(Enum):
    civil = 'civil'
    chemical = 'chemical'
    electrical = 'electrical'
    mechanical = 'mechanical'
    software = 'software'
    materials = 'materials'
    engphys = 'engphys'


## @brief Datatype for student information
#  @details NamedTuple datatype for students
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
