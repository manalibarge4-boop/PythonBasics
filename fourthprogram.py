#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      manal
#
# Created:     03-10-2026
# Copyright:   (c) manal 2026
# Licence:     <your licence>
#-------------------------------------------------------------------------------

age = input("enter your age")

if int(age) >= 18:
    print("You can vote")
elif int(age) <= 18 and int(age) >=3 :
    print("you are in school")
else :
    print("you are a child")