from Sample_Data_Structure import Students

from re import X


All_assignments = {'Assignments 1': 45, 'Assignment 2' : 50, 'Assignment 3' : 75, 'Assignment 4' : 90, 'Assignment 5' : 55} 
Assignments = []
#print Assignments()

def assignment_filter(All_assignments:dict):
    """Filter through posted aassignments and remove any over 60%"""
    for key in All_assignments.keys():
        Assignment = All_assignments.get(key,X)
        if Assignment <= 60:
            Assignments.append(key) 


def display_assignment(Assignments:list): 
    """Print each Assignment idividually"""
    for Assignment in Assignments: 
        print (f"* {Assignment}")

    

def apr_generator(): 
    """This function will access List of APR'S and create them"""
    current_grade = 60 
    Student_name = "Luke"  
    Class = "CMPSC 300" 
    days_missed = 12
    #Assignments = {'Assignments_1': 45, 'Assignment_2' : 50, 'Assignment_3' : 75, 'Assignment_4' : 90, 'Assignment_5' : 55} 
    print(f"Hello {Student_name}, This is a notice that you are receiving an academic alert in CMPSC 300. You currently have a {current_grade} in this class as you are either missing or received less than a 60% on these assignments: ")
    display_assignment(Assignments)
    print(f"you have missed {days_missed} days. If this continues you may be in danger of failing this course, please reach out to me to see how you can bring this up, and get back on track for success!")
assignment_filter(All_assignments)
apr_generator() 
