# Question-2:
# Assume, you are given two dictionaries. The dictionary named 
# current_sem_data contains the GPA of 3 students of their current semester 
# courses. The dictionary named previous_sem_data contains their previous 
# semesters’ CGPA and credits completed respectively. Assume that all courses 
# are of 3 credits each.

# current_sem_data = 
# {"John":[4.0,3.7,4.0], "Tom":[3.3,3.7,4.0], "Harry":[3.3,3.7,4.0]}
# previous_sem_data = {"John":[3.88,90], "Tom":[3.52, 70], "Harry":[3.25,85]}

# Now, write a Python program that will take a student’s name as user input 
# and calculate and print that student’s current CGPA using both the given 
# dictionaries.
# FORMULA for calculating CGPA:
# current_total_GPA= ∑ (current course grade X credit)
# previous_total_GPA= Previous CGPA* total credits previously
# C.G.P.A = (current_total_GPA + previous_total_GPA)/(Total Credits completed 
# till current semester)
# =======================================================
# Sample Input 1:
# John

# Sample Output 1:
# ****Data for John****
# Previous semester's completed credits: 90
# Previous semester's CGPA: 3.88
# Total Credits completed including current semester: 99
# Current semester's total GPA: 35.1
# Current semester's CGPA: 3.881818181818182


name = input("Enter student name: ")
current_sem_data = {"John":[4.0,3.7,4.0], "Tom":[3.3,3.7,4.0], "Harry":[3.3,3.7,4.0]}
previous_sem_data = {"John":[3.88,90], "Tom":[3.52, 70], "Harry":[3.25,85]}

prev_credit = previous_sem_data[name][1]
cur_cg = current_sem_data[name]
CCGPA = 0
for i in cur_cg:
	CCGPA += 3*i

prev_cg = prev_credit*previous_sem_data[name][0]

TCG = (CCGPA+prev_cg)/(prev_credit+9)

print(f"****Data for {name}****")
print("Previous semester's completed credits: ", prev_credit)
print("Total Credits completed including current semester: ",prev_credit+9)
print("Current semester's total GPA: ", CCGPA)
print("Current semester's CGPA: ", TCG)