from Sample_Data_Structure import Students

from gmail_api.send_emails import send_message
from gmail_api.send_emails import gmail_authenticate

# from access_sheets import master_dict

import superuser

from re import X

def assignment_filter(All_assignments:dict):
    """Filter through posted assignments and remove any over 60%"""
    for key in All_assignments.keys():
        Assignment = All_assignments.get(key,X)
        if Assignment <= 60:
            Assignments.append(key)   

def apr_generator(current_grade: int, student_name: str, assigned_class: str, days_missed: int): 
    """This function will access List of APR'S and create them"""
    with open((str(student_name) + '_apr.txt'), 'w') as f:
        print(f"Hello {student_name}, This is a notice that you are receiving an academic alert in {assigned_class}. ", file = f)
        print(f"You currently have a {current_grade} in this class as you are either missing or received less than a 60% on these assignments:", file = f)
        global Assignments
        for Assignment in Assignments: 
            print (f"* {Assignment}", file = f)
        print(f"you have missed {days_missed} days. If this continues you may be in danger of failing this course, please reach out to me to see how you can bring this up, and get back on track for success!", file = f)
        

if __name__ == '__main__':
    Assignments = []
    for i in range(len(Students) - 1):
        if superuser.compare_stu_super(Students['Student_' + str(i + 1)]['Total']) == True:
            assignment_filter(Students['Student_' + str(i+1)]['Assignments'])
            apr_generator(Students['Student_' + str(i+1)]['Total'], Students['Student_' + str(i+1)]['Name'], 
            Students['Student_' + str(i+1)]['Assigned Class'], Students['Student_' + str(i+1)]['Days Missed'])
            service = gmail_authenticate()
            email_subject = "Notice on missing " + str(Students['Student_' + str(i+1)]['Assigned Class']) + " for" + str(Students['Student_' + str(i+1)]['Name'])
            email_intro = "Dear " + str(Students['Student_' + str(i+1)]['Name']) + ", " + "\n" + "\n"
            email_body = email_intro + "You have received this APR due to academic performance in " + str(Students['Student_' + str(i+1)]['Assigned Class']) + ". Please check this APR to on what you are missing in this class. "
            send_message(service, Students['Student_' + str(i+1)]['Student Email'], email_subject, 
    email_body, [str(Students['Student_' + str(i+1)]['Name']) + '_apr.txt'], Students['Student_' + str(i+1)]['Advisor Email'], Students['Student_' + str(i+1)]['Professor Email'])
