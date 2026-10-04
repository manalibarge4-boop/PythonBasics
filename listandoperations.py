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

marks = [95, 98, 97]
print(marks)

marks = [95, 98, 97]
print(marks[0])

marks = [95, 98, 97] # 0=95, 1=98, 2=97 but to will not display as the range given
print(marks[0:2])

marks = [95, 98, 97]
for score in marks:
    print(score)

marks = [95, 98, 97] #to insert value in last only
marks.append(99)
print(marks)

marks = [95, 98, 97] #to insert value in middle or first
marks.insert(0, 99)
print(marks)

marks = [95, 98, 97]
marks.insert(1, 99)
print(marks)
print(99 in marks) #to see if the number exist in the list or not
print(len(marks)) #to see the number of elements in the list

i = 0
while i <len(marks):
    print(marks(i))
    i = i + 1

marks.clear()
print(marks)