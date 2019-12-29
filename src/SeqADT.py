## @file SeqADT.py
#  @author Zayed Sheet
#  @brief Abstract data type that represents sequence for list of choices
#  @date 2019-02-11


## @brief Class for abstract data type that represents sequence for list of choices
#  @details Class for ADT that treats list of choices as a sequence
class SeqADT:

    ## @brief initializer for class that sets index to 0 and s to inputted list
    def __init__(self, x):
        self.__s = x  # s and i are state variables
        self.__i = 0  # __ is so you can access the state variables directly

    ## @brief sets the index of the data type to 0
    def start(self):  # pass in self if you're changing state variables
        self.__i = 0

    ## @brief method that allows user to access next item in list
    #  @return returns the next item in the list
    def next(self):
        if self.__i < len(self.__s):
            self.__i += 1
            return self.__s[self.__i - 1]
        else:
            raise StopIteration

    ## @brief method that lets user know if they're at the end of the list
    #  @return returns True if user is at end of list, otherwise false
    def end(self):
        if self.__i < len(self.__s):
            return False
        return True
