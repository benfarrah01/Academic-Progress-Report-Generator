""""This file, when put into `SheetShuttle/plugins`, can be run to display the contents of the sheet."""
from sheetshuttle import sheet_collector
import pandas as pd
#from sheetshuttle import Sheet

# File containing authentication information. DON'T PUSH `new_key.json` TO GITHUB!!!
key_file='new_key.json'
# Directory containing config information for our google sheet
sources_dir='config/sheet_sources'

def run(sheets_keys_file, sheets_config_directory, **kwargs):
     global master_dict
     """Example run function. Collect and display info from google sheet."""
     # Create SheetCollector object named `my_collector`
     #   Created with args `key_file` and `sources_dir`
     my_collector = sheet_collector.SheetCollector(key_file, sources_dir)
     my_collector.collect_files()

     # collect data from each region of each sheet
     my_data = my_collector.sheets_data["APR-Generator-Config"].regions["Sheet1_Students_Info"].data  

     # convert data to a dictionary
     dict_data = my_data.to_dict()
     
     # create new dictionary of dictionaries with a specified structure
     for count in range(len(dict_data["Name"])):
          # create initial dict
          if count == 0:
               master_dict = make_dict(
                    dict_data["Class"][count],
                    dict_data["Attendance"][count],
                    dict_data["Name"][count],
                    dict_data["Email"][count],
                    dict_data["Advisor"][count],
                    dict_data["Advisor Email"][count],
                    dict_data["Total"][count],
               )
          # add to initial dict
          else:
               my_dict = add_info_to_dict(
                    master_dict,
                    dict_data["Class"][count],
                    dict_data["Attendance"][count],
                    dict_data["Name"][count],
                    dict_data["Email"][count],
                    dict_data["Advisor"][count],
                    dict_data["Advisor Email"][count],
                    dict_data["Total"][count],
               )

     for k in master_dict:
          # display key
          print(k)
          # nested dict at each key
          print(master_dict[k])
          print()

     
     print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

     # name_input = input("Enter a name: ")
     # for i in range(len(master_dict)):
     #      if name_input == master_dict[i]:
     #           austin_powers(master_dict[i])


     

               
# accept data to create nested dict with specific format
def make_dict(classname, studentattendance, studentname, studentemail, advisorname, advisoremail, points):
     my_dict = {
          studentname: {
               "Class": classname,
               "Attendance": studentattendance,
               "Email": studentemail,
               "Advisor": advisorname, 
               "Advisor_Email": advisoremail, 
               "total": points}, 
     }
     return my_dict

# update nested dict with new values (turn new values into dict before updating nested dict)
def add_info_to_dict(master_dict, lassname, studentattendance, studentname, studentemail, advisorname, advisoremail, points):
     my_dict = make_dict(lassname, studentattendance, studentname, studentemail, advisorname, advisoremail, points)
     master_dict.update(my_dict)

# updated nested dict with new dict
def add_dict_to_dict(master_dict, my_dict):
     master_dict.update(my_dict)


