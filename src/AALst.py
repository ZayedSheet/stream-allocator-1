## @file AAlst.py
#  @author Zayed Sheet
#  @brief This module is for the AALst data type
#  @date 2019-02-11


from StdntAllocTypes import *


## @brief Class for AALst data type
#  @details This datatype has methods for intializing, adding an allocated student
#           \n and returning the list of allocated students or how many students are
#           \n allocated into a department
class AALst:

    ## @brief  Initializes the data type
    #  @details Creates a list of tuples containing department and an empty list
    @staticmethod
    def init():  # initialize list
        AALst.s = []
        for i in DeptT:
            AALst.s.append((i, []))

    ## @brief Adds a student to the datatype
    #  @details Adds a student into their desired department
    #  @param dep the department user is being allocated to
    #  @param m the user's macid
    @staticmethod
    def add_stdnt(dep, m):
        for i in AALst.s:
            if dep in i:
                i[1].append(m)

    ## @brief Returns the list of students allocated into a department
    #  @param d The desired department of type DeptT
    #  @return The list of students allocated into a department
    @staticmethod
    def lst_alloc(d):
        for i in AALst.s:
            if d in i:
                return i[1]

    ## @brief Returns how many students are allocated into a specific department
    #  @param d The department of type DeptT
    #  @return The number of students allocated into a department
    @staticmethod
    def num_alloc(d):
        for i in AALst.s:
            if d in i:
                return len(i[1])
