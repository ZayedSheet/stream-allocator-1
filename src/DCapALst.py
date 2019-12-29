## @file DCapALst.py
#  @author Zayed Sheet
#  @brief This module is for the DCapALst data type for eng streams
#  @date 2019-02-11


## @brief Class for datatype for department and department capacities
class DCapALst:

    ## @brief Intiializes a list for the class
    @staticmethod
    def init():  # initialize list
        DCapALst.s = []

    ## @brief Adds a department and its capacity into the list
    #  @details Adds a tuple containing the department as a DeptT type and the capacity for
    #  @        \n that department
    #  @param d department name as a DeptT type
    #  @param n Integer for capacity for department
    @staticmethod
    def add(d, n):
        for department in DCapALst.s:
            if d in department:  # if the program is not already in the list
                raise KeyError
        DCapALst.s.append((d, n))

    ## @brief Removes a department from the list
    #  @param d Department as a DeptT type
    @staticmethod
    def remove(d):
        for department in DCapALst.s:  # for every tuple in s
            if d in department:  # if the department is in this tuple
                DCapALst.s.remove(department)  # remove the tuple from the list
                return  # exit the function
        raise KeyError

    ## @brief Checks if a department exists in the list
    #  @param Department as a DeptT data type
    #  @return Returns true if department exists otherwise false
    @staticmethod
    def elm(d):
        for department in DCapALst.s:  # for every department tuple in s
            if d in department:  # if the department is in this tuple
                return True
        return False

    ## @brief Checks the capacity for a department
    #  @param d Department as a DeptT type
    @staticmethod
    def capacity(d):
        for department in DCapALst.s:  # for every tuple in s
            if d in department:  # if the department is in this tuple
                return department[1]
        raise KeyError
