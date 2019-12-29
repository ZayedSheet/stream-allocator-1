## @file DCapALst.py
#  @author Justin Rosner, rosnej1
#  @brief Setting the department capacities for each engineering faculty
#  @date 02/05/2019

from StdntAllocTypes import *
from typing import NamedTuple


## @brief This class defines the tuple (dept: DeptT, cap: N)
class _DepartmentCapT(NamedTuple):
    dept: DeptT
    cap: int


## @brief An abstract object for storing the department capacities
class DCapALst:

    # A set of tuples defined as (dept: DeptT, cap: N)
    s = set()

    ## @brief Initialize empty data structure
    @staticmethod
    def init():
        DCapALst.s = set()

    ## @brief Adds a department and its capacity to the list
    #  @param d represents a department of type DeptT
    #  @param n is an integer representing the capacity of the department
    #  @throw Throws KeyError when the user tries to add a duplicate key
    @staticmethod
    def add(d, n):
        for department in DCapALst.s:
            if department.dept == d:
                raise KeyError
        DCapALst.s.add(_DepartmentCapT(d, n))

    ## @brief Deletes a department and its corresponding capacity from the list
    #  @param d represents a department of type DeptT
    #  @throw Throws KeyError when the department the user wants to delete is
    #  not in the current department list
    @staticmethod
    def remove(d):
        for department in DCapALst.s.copy():
            if department.dept == d:
                DCapALst.s.remove(department)
                return
        raise KeyError

    ## @brief Checks to see if an element already exists in the list
    #  @param d represents a department of type DeptT
    #  @return True if the element exists, and False if it does not
    @staticmethod
    def elm(d):
        for department in DCapALst.s:
            if department.dept == d:
                return True
        return False

    ## @brief Gives the user back the department capacity of thier choosing
    #  @param d represents a department of type DeptT
    #  @throw Throws KeyError if the department of choosing is not in the list
    #  @return Returns an integer value representing the capacity of the department
    @staticmethod
    def capacity(d):
        for department in DCapALst.s:
            if department.dept == d:
                return department.cap
        raise KeyError
