## @file SeqADT.py
#  @author Justin Rosner, rosnej1
#  @brief Defining a class to store student choices
#  @date 02/06/2019


## @brief An abstract data type that iterates through a sequence
class SeqADT:

    ## @brief SeqADT constructor
    #  @details Takes a sqeuence of type T and returns an ADT that allows the
    #  user to iterate through a sequence
    #  @param x is a sequence of type T
    def __init__(self, x):

        self.__s = x
        self.__i = 0

    ## @brief start sets the counter back to 0 (ie. the start)
    def start(self):
        self.__i = 0

    ## @brief Iterates to the next element in the sequence
    #  @throw Throws StopIteration exception when i goes out of range
    #  @return Returns the next element in the sequence
    def next(self):
        if self.__i >= len(self.__s):
            raise StopIteration
        else:
            temp = self.__i
            self.__i += 1
            return (self.__s[temp])

    ## @brief Checks to see if the sequence is at the end
    #  @return A boolen value of True or False
    def end(self):
        if self.__i < len(self.__s):
            return False
        else:
            return True
