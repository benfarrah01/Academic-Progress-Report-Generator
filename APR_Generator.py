#from Sample_Data_Structure import Students

# from gmail_api.send_emails import send_message
# from gmail_api.send_emails import gmail_authenticate
from sheetshuttle import sheet_collector

#from access_sheets import master_dict

#import superuser

from re import X

# File containing authentication information. DON'T PUSH `new_key.json` TO GITHUB!!!
key_file='new_key.json'
# Directory containing config information for our google sheet
sources_dir='config/sheet_sources'

def run(sheets_keys_file, sheets_config_directory, **kwargs):
     #global master_dict
     """Example run function. Collect and display info from google sheet."""
     # Create SheetCollector object named `my_collector`
     #   Created with args `key_file` and `sources_dir`
     my_collector = sheet_collector.SheetCollector(key_file, sources_dir)
     my_collector.collect_files()

     # collect data from each region of each sheet
     region_info = my_collector.sheets_data["APR-Generator-Config"].regions["Example_Students_Info"].data  
     region_grades = my_collector.sheets_data["APR-Generator-Config"].regions["Example_Students_Grades"].data  

     # convert data to a dictionary
     my_dictionary_sorter = data_to_dict(region_info,region_grades)
     
     my_dictionary_sorter.sorted_dict()

     Students = my_dictionary_sorter.master_dict



     Assignments = []
     lessthan60 = []
     my_keys = []
     for key in Students.keys():
          my_keys.append(key)
     for i in range(len(Students.keys()) - 1):
          current = my_keys[i+1]
          if compare_stu_super(Students[current]['Total'], Students["Super User"]) == True:
               Assignments.append(assignment_filter(Students[current]['Assignments']))             
               
               
               apr_generator(
                    Students[current]['Total'], 
                    Students[current]['Name'], 
                    Students[current]['Assigned Class'], 
                    Students[current]['Days Missed'],
                    Assignments
               )

               service = gmail_authenticate()
               email_subject = "Notice on missing " + str(Students['Student_' + str(i+1)]['Assigned Class']) + " for" + str(Students['Student_' + str(i+1)]['Name'])
               email_intro = "Dear " + str(Students[current]['Name']) + ", " + "\n" + "\n"

               email_body = email_intro + "You have received this APR due to academic performance in " + str(Students['Student_' + str(i+1)]['Assigned Class']) + ". Please check this APR to on what you are missing in this class. "
               
               send_message(service, Students['Student_' + str(i+1)]['Student Email'], email_subject, email_body, [str(Students['Student_' + str(i+1)]['Name']) + '_apr.txt'],Students['Student_' + str(i+1)]['Advisor Email'], Students['Student_' + str(i+1)]['Professor Email'])


# begin DATA_TO_DICT class
class data_to_dict:
     def __init__(self, region_info,region_grades):
          self.region_info = region_info
          self.region_grades = region_grades
          self.master_dict = {}

     def sorted_dict(self):
          # convert data to dictionary
          info_data = self.region_info.to_dict()
          grades_data = self.region_grades.to_dict()

          # create new dictionary of dictionaries with a specified structure
          for count in range(len(info_data["Student Name"])):
               # create initial dict
               if count == 0:
                    self.master_dict = self.make_dict(
                         info_data["Class"][count],
                         info_data["Professor"][count],
                         info_data["Professor Email"][count],
                         info_data["Attendance"][count],
                         info_data["Student Name"][count],
                         info_data["Student Email"][count],
                         info_data["Advisor"][count],
                         info_data["Advisor Email"][count],
                         [
                              grades_data["Total"][count],
                              grades_data["Assignment 1"][count],
                              grades_data["Assignment 2"][count],
                              grades_data["Assignment 3"][count],
                              grades_data["Assignment 4"][count],
                              grades_data["Assignment 5"][count],
                              grades_data["Assignment 6"][count],
                              grades_data["Assignment 7"][count],
                              grades_data["Assignment 8"][count],
                              grades_data["Assignment 9"][count],
                              grades_data["Assignment 10"][count],
                              grades_data["Assignment 11"][count],
                              grades_data["Assignment 12"][count],
                         ],
                    )
                    
               # add to initial dict
               else:
                    my_dict = self.add_data_to_dict(
                         self.master_dict,
                         info_data["Class"][count],
                         info_data["Professor"][count],
                         info_data["Professor Email"][count],
                         info_data["Attendance"][count],
                         info_data["Student Name"][count],
                         info_data["Student Email"][count],
                         info_data["Advisor"][count],
                         info_data["Advisor Email"][count],
                         [
                              grades_data["Total"][count],
                              grades_data["Assignment 1"][count],
                              grades_data["Assignment 2"][count],
                              grades_data["Assignment 3"][count],
                              grades_data["Assignment 4"][count],
                              grades_data["Assignment 5"][count],
                              grades_data["Assignment 6"][count],
                              grades_data["Assignment 7"][count],
                              grades_data["Assignment 8"][count],
                              grades_data["Assignment 9"][count],
                              grades_data["Assignment 10"][count],
                              grades_data["Assignment 11"][count],
                              grades_data["Assignment 12"][count],
                         ],
                    )

     def make_dict(self,_class, _professor, _professoremail, _attendance, _studentname, _studentemail, _advisor, _advisoremail, _grades):
          my_dict = {
               _studentname: {
                    "Total": _grades[0],
                    "Name": _studentname,
                    "Student Email": _studentemail,
                    "Assignments": {
                         "Assignment 1": _grades[1],
                         "Assignment 2": _grades[2],
                         "Assignment 3": _grades[3],
                         "Assignment 4": _grades[4],
                         "Assignment 5": _grades[5],
                         "Assignment 6": _grades[6],
                         "Assignment 7": _grades[7],
                         "Assignment 8": _grades[8],
                         "Assignment 9": _grades[9],
                         "Assignment 10": _grades[10],
                         "Assignment 11": _grades[11],
                         "Assignment 12": _grades[12],
                         },
                    "Assigned Class": _class,
                    "Days Missed": _attendance,
                    "Advisor": _advisor,
                    "Advisor Email": _advisoremail,
                    "Professor": _professor,
                    "Professor Email": _professoremail,
                    }
          }
          return my_dict

     def add_data_to_dict(self, master_dict, _class, _professor, _professoremail, _attendance, _studentname, _studentemail, _advisor, _advisoremail, _grades):
          my_dict = self.make_dict(_class, _professor, _professoremail, _attendance, _studentname, _studentemail, _advisor, _advisoremail, _grades)
          master_dict.update(my_dict)

     def display_dict(self):
          for k in self.master_dict:
               # display key
               print(k)
               # nested dict at each key
               print(self.master_dict[k])
               print()
# end DATA_TO_DICT class



def assignment_filter(student_assignments):
     """Filter through posted assignments and remove any over 60%"""
     #     for key in All_assignments.keys():
     #         Assignment = All_assignments.get(key,X)
     #         if Assignment <= 60:
     #             Assignments.append(key)   
     for assn in student_assignments:
          if int(student_assignments[assn]) < 60:
               return(assn)

def apr_generator(current_grade: int, student_name: str, assigned_class: str, days_missed: int, Assignments: list[str]): 
    """This function will access List of APR'S and create them"""
    with open((str(student_name) + '_apr.txt'), 'w') as f:
        print(f"Hello {student_name}, This is a notice that you are receiving an academic alert in {assigned_class}. ", file = f)
        print(f"You currently have a {current_grade} in this class as you are either missing or received less than a 60% on these assignments:", file = f)
        for Assignment in Assignments: 
            print (f"* {Assignment}", file = f)
        print(f"you have missed {days_missed} days. If this continues you may be in danger of failing this course, please reach out to me to see how you can bring this up, and get back on track for success!", file = f)
        

# gmail_api send_emails

import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
our_email = 'team0neapr@gmail.com'

def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
# service = gmail_authenticate()

# Adds the attachment with the given filename to the given message
def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

def build_message(destination, obj, body, attachments=[], cc1 = None, cc2 = None):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
        message['cc'] = cc1
        message['cc'] = cc2
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
        message['cc'] = cc1
        message['cc'] = cc2
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, destination, obj, body, attachments=[], cc1 = None, cc2 = None):
    return service.users().messages().send(
    userId="me",
    body=build_message(destination, obj, body, attachments, cc1, cc2)
    ).execute()


    # test send email
# send_message(service, "anargya01@allegheny.edu", "This is a subject", 
# "This is the body of the email", ["test.txt"])


#superuser
# from Sample_Data_Structure import Students
import sys

#data = Students

def compare_stu_super(total_value, superuser):
     #k = 0
     #print(superuser.items())
     # for p_id, p_info in superuser.items():
     #      if p_id == "Superuser":
     #           for key in p_info:
     #                if key == "Total":
     #                     k = p_info.get(key,0)
     k = float(superuser["Total"])
     print(total_value)
     if float(total_value)/k < 0.7:
          return True
     else:
          return False
