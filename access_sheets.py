""""This file, when put into `SheetShuttle/plugins`, can be run to display the contents of the sheet."""
from sheetshuttle import sheet_collector

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
     my_dictionary = data_to_dict(region_info,region_grades)
     my_dictionary.sorted_dict()
     my_dictionary.display_dict()

               
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