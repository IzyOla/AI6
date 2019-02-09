# AI6 Assignment 1
dict = {'fullName': 'Israel Oladejo', 'reasonForAttendingAISaturday': 'I want to learn techniques to visualize data and manipulate such data to solve critical problems in my society using artificail intelligence.'}
print "My name is " + (dict['fullName']) + " and at the end of this cohort I want to " + (dict['reasonForAttendingAISaturday']) 

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Even numbers in the list: ", count_even,)
print("Odd numbers in the list: ", count_odd)