#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      manal
#
# Created:     04-10-2026
# Copyright:   (c) manal 2026
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Tuple is immutable, we cant change or do operations in tuple.
#when we make tuple we cant change it.
#its not necesarry to apply ()parenthesis in tuple

marks = (95, 98, 97, 92)
print(marks)

marks = (95, 98, 97, 97, 97, 92)
print(marks.count(97))  #but it can able to count how many times the elements are present in tuple

print(marks.index(97)) #it will print the index of the element,, like in this
                       #if there are two same element it will print which comes first