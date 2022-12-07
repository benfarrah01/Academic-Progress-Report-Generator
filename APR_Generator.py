from Sample_Data_Structure import Students

from re import X

from typing import List
# from typing import Dict


# All_assignments = {'Assignments 1': 45, 'Assignment 2' : 50, 'Assignment 3' : 75, 'Assignment 4' : 90, 'Assignment 5' : 55} 
Assignments = []
#print Assignments()

def assignment_filter(All_assignments:dict):
    """Filter through posted aassignments and remove any over 60%"""
    for key in All_assignments.keys():
        Assignment = All_assignments.get(key,X)
        if Assignment <= 60:
            Assignments.append(key)


def display_assignment(Assignments:List[int]): 
    """Print each Assignment individually"""
    for Assignment in Assignments: 
        print (f"* {Assignment}")

    

def apr_generator(current_grade: int, student_name: str, assigned_class: str, days_missed: int): 
    """This function will access List of APR'S and create them"""
    # current_grade = 60 
    # Student_name = "Luke"  
    # assigned_class = "CMPSC 300" 
    # days_missed = 12
    # Assignments = {'Assignments_1': 45, 'Assignment_2' : 50, 'Assignment_3' : 75, 'Assignment_4' : 90, 'Assignment_5' : 55} 
    print(f"Hello {student_name}, This is a notice that you are receiving an academic alert in {assigned_class}. You currently have a {current_grade} in this class as you are either missing or received less than a 60% on these assignments: ")
    display_assignment(Assignments)
    print(f"you have missed {days_missed} days. If this continues you may be in danger of failing this course, please reach out to me to see how you can bring this up, and get back on track for success!")

if __name__ == '__main__':
    assignment_filter(Students['Student_2']['Assignments'])
    apr_generator(Students['Student_2']['Current Grade'], Students['Student_2']['Name'], 
    Students['Student_2']['Assigned Class'], Students['Student_2']['Days Missed'])
    # assignment_filter(All_assignments)
    # apr_generator() 
