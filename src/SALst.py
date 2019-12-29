## @file SALst.py
#  @author Zayed Sheet
#  @brief This module is for the SALst data and is mainly used to allocate students
#  @date 2019-02-11


from AALst import *
from DCapALst import *


## @brief Class for allocating students into programs
#  @details This class allocated students into their programs based off several aspects
#           \n like if its full or not. The class has several different methods to do this
#           \n including sort, remove, allocate.
class SALst:

    ## @brief Initializes a list for list of students
    @staticmethod
    def init():
        SALst.s = []

    ## @brief Adds a student into the list of students
    #  @param m Students macid
    #  @param i Students information of type SinfoT
    @staticmethod
    def add(m, i):
        for student in SALst.s:  # for every element in SALst
            if m in student:  # if the macid is present in that element
                raise KeyError
        SALst.s.append((m, i))  # otherwise append student to the list

    ## @brief Removes a student from the list
    #  @param m Students macid
    @staticmethod
    def remove(m):
        for student in SALst.s:  # for every student in SAlst
            if m in student:  # if the given macid is in this tuple
                SALst.s.remove(student)  # remove that student from the list
                return  # exit function
        raise KeyError  # otherwise if macid isn't present anywhere, raise keyerror

    ## @brief Checks if a student is in the list
    #  @param m Students Macid
    #  @return Returns true or false based off whether student is in student list
    @staticmethod
    def elm(m):
        for student in SALst.s:  # for every student in s list
            if m in student:  # if student has the given macid
                return True  # return true
        return False  # otherwise if no student has this macid return false

    ## @brief Returns a students information
    #  @param m Students Macid
    #  @return Students information as a data type SinfoT
    @staticmethod
    def info(m):
        for student in SALst.s:  # for every student in s list
            if m in student:  # if student has the given macid
                return student[1]  # return student SinfoT
        raise KeyError  # otherwise if no student has this macid return exception

    ## @brief Filters and sorts the list of students based off gpa
    #  @details Sorts the students in student list based off their GPA first. Then filters the
    #  @students based off the function passed in as a parameter.
    #  @param f Function passed in to filter students based off function requirements
    #  @return Returns the list of sorted and filtered students
    @staticmethod
    def sort(f):
        SALst.sorted_list = []  # initialize sorted list variable

        a_list = sorted(SALst.s, key=lambda x: x[1].gpa, reverse=True)  # sort the list

        for student in a_list:  # for every student in filtered list
            if f(student[1]):  # if the student meets the function requirements
                SALst.sorted_list.append(student[0])  # add that student's macid to the list

        return SALst.sorted_list

    ## @brief Calculated the average GPA of students based off the passed in function's
    #         \n requirements
    #  @param f Function passed in to filter students based off function requirements
    #  @return Returns the average GPA
    @staticmethod
    def average(f):
        total = 0
        num_student = 0
        for student in SALst.s:
            if f(student[1]):
                total += student[1].gpa
                num_student += 1
        if num_student == 0:
            raise ValueError
        return total / num_student

    ## @brief Allocates students into their program based off several factor
    #  @details Allocates students into their program. It first prioritizes students with
    #           \n free choice, then allocates students in order of highest to lowest GPA.
    #           \n students who failed are not allocated and filtered out. The AALst data
    #           \n type is used for all allocation.
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for student in f:
            ch = SALst.info(student).choices
            AALst.add_stdnt(ch.next(), student)

        s = SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while not alloc and not ch.end():
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
                if not alloc:
                    raise RuntimeError
