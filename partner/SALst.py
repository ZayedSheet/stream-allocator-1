## @file SALst.py
#  @author Justin Rosner, rosnej1
#  @brief Student Allocation Module
#  @date 02/09/2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *
from operator import itemgetter


## @brief This function gets the GPA of a desired student
#  @param m is a string representing a students macid
#  @param s is a set of type StudentT
#  @return a float representing the gpa of the student
def _get_gpa(m, s):
    if m in s:
        return (s[m].gpa)


## @brief An abstract object for allocating students into their second year streams
class SALst:

    # A dictionary of StudentT which is a tuple of (macid: string, info: SInfoT)
    s = {}
    ## @brief Initializes the empty data structure
    @staticmethod
    def init():
        AALst.init()
        SALst.s = {}

    ## @brief This function adds a student to the list s
    #  @param m is a string representing the students macid
    #  @param i is information about the student of type SInfoT
    #  @throw Throws KeyError if macid is already in the list
    @staticmethod
    def add(m, i):
        if m in SALst.s:
            raise KeyError
        SALst.s[m] = i

    ## @brief This function removes a student from the list s
    #  @param m is a string representing the students macid
    #  @throw Throws KeyError if the student is not in the list
    @staticmethod
    def remove(m):
        if m in SALst.s:
            del SALst.s[m]
            return
        raise KeyError

    ## @brief This function checks to see if a student is already in the list
    #  @param m is a string representing the macid of a student
    #  @return A boolean value True if the macid is in the list and False if not
    @staticmethod
    def elm(m):
        if m in SALst.s:
            return True
        return False

    ## @brief This function gets the information about the student
    #  @param m is a string representing a students macid
    #  @throw Throws an exception ValueError when the student is not in the list
    #  @return Returns the information (SInfoT) of the student
    @staticmethod
    def info(m):
        if m in SALst.s:
            return (SALst.s[m])
        raise KeyError

    ## @brief This function returns a list of students sorted by gpa
    #  @param f is a lambda function that checks if a student has free choice and a gpa >= 4.0
    #  @return A sequence of students in order of decreasing gpa
    @staticmethod
    def sort(f):
        unsorted_list = []
        sorted_list = []

        # Iterate through the list of type StudentT
        for student in SALst.s:
            if f(SALst.s[student]):
                # Make a temp dict that contains macid and gpa and append this to a list
                temp_dict = {'macid': student,
                             'gpa': _get_gpa(student, SALst.s)}
                unsorted_list.append(temp_dict)

        temp_list = sorted(unsorted_list, key=itemgetter('gpa'), reverse=True)

        # Go through the now sorted list and append just the macid to the final list
        for element in temp_list:
            sorted_list.append(element['macid'])

        return (sorted_list)

    ## @brief This function returns the gpa of a gender specific set of students
    #  @param f is a lambda function that checks the gender of the student
    #  @throw Throws ValueError when the gender specific subset of students is NULL
    #  @return A float value representing the average gpa of a specified subset
    #  of students
    @staticmethod
    def average(f):
        total_gpa = 0.0
        count = 0

        for student in SALst.s:
            if f(SALst.s[student]):
                total_gpa += _get_gpa(student, SALst.s)
                count += 1

        if count == 0:
            raise ValueError

        return (total_gpa / count)

    ## @brief This function allocates the students into their upper year programs
    #  @throw Throws RuntimeError if student runs out of choices
    @staticmethod
    def allocate():
        # Adding students with freechoice to their department
        freechoice_list = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for macid in freechoice_list:
            ch = SALst.info(macid).choices
            AALst.add_stdnt(ch.next(), macid)

        # Adding the students with no free choice to their department
        normal_student_list = SALst.sort(lambda t: not(t.freechoice) and t.gpa >= 4.0)
        for macid in normal_student_list:
            ch = SALst.info(macid).choices
            alloc = False

            while (not(alloc) and not(ch.end())):
                dept = ch.next()
                if (AALst.num_alloc(dept) < DCapALst.capacity(dept)):
                    AALst.add_stdnt(dept, macid)
                    alloc = True

            if (not(alloc)):
                raise RuntimeError
