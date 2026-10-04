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

#set is the collection of elements which is used to store
#it stores only unique values, not duplicates

marks = {95, 98, 97, 97, 97, 92}
print(marks) #97 will print only one time as set didnt stores duplicate values

#print(marks[0]) #will display error as it doesnt display index, it stores the element randomly

for scores in marks:
    print(scores) #since there is no index in sets and displays randomly they also called unordered