## @file Read.py
#  @author Zayed Sheet
#  @brief This file contains functions that extracts student/department data from text files.
#  @date 2019-02-11


from SALst import *
import re


## @brief Uses the data from a text file to add all students
#  @details Reads from a text file and uses the data to create
#  @param s This parameter is a text file that contains a student on each line.
def load_stdnt_data(s):
    f = open(s, "r")
    lines = f.read().splitlines()
    f.close()
    SALst.init()
    dept = []
    free = True

    for i in lines:
        s = re.split(', \[|\], |, ', i)
        for i in range(5, len(s)-1):
            dept.append(DeptT(s[i]))

        if s[len(s)-1] == "True":
            free = True
        else:
            free = False

        info = SInfoT(s[1], s[2], GenT(s[3]), float(s[4]), SeqADT(dept), free)
        SALst.add(s[0], info)


## @brief  Obtains information on the engineering streams and their respective capacities.
#  @param s This parameter is a text file that contains the engineering streams
def load_dcap_data(s):
    DCapALst.init()
    with open(s, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        for i in range(len(lines)):  # for every line
            dept = lines[i].split(', ')  # creates a list with department and capacity
            temp = DeptT(dept[0])
            DCapALst.add(temp, int(dept[1]))
    f.close()
