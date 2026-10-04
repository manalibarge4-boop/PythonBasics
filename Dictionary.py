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

#Dictionary stores elements in key-value pairs

marks = {"English" : 95, "Chemistry" : 92}

#how to access the information in dictionary
print(marks["Chemistry"])

#to add new info
marks["Physics"] = 97;
print(marks)

#we can also able to change the information
marks["Physics"] = 99;
print(marks)
