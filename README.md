# apr-generator-plugin

## Contributors

- Makell Logan : https://github.com/Makell-Logan
- Bergas Anargya : https://github.com/bergasanargya
- Ben Farrah : https://github.com/benfarrah01
- Darius Googe : https://github.com/Darius90332
- Luke Barker : https://github.com/Barker0103

Documentation Website: https://sites.google.com/allegheny.edu/apr-generator-plugin/home 

## Description
This is a plugin created for [sheetshuttle](https://github.com/GatorEducator/SheetShuttle). At our client's request we created a plugin to gather data from a google sheet containing a Professor's gradebook. Our program sorts through that data, figuring out which students aren't doing well (If their overall grade is less than a 70%) then write a Academic Progress Report, that gives them a warning, telling them how many days they've missed and what assignments they didn't do well on (Received a score less than 60%), encouraging them to reach out to the Professor and see what they can do to improve their grade. It then sends out that report as a email to the student and their advisor. 


### In order to make this possible we used:
- Python
- SheetShuttle
- The Google Sheets API
- The Gmail API


### These are some challenges we faced, while designing this plugin:
- We struggled with converting the google sheet into a dictionary that we could access in our `APR-generator.py` as we didn't have much experience with it.
- We had never used the Gmail API, so that we had to research and learn about it first before we could implement it.
- We never used Mkdocs before, so we had trouble getting the docstings onto the web pages. So instead we opted to use google sites.

## How To Use Our Plugin
1. Clone the [sheetshuttle](https://github.com/GatorEducator/SheetShuttle) repository
2. Clone this repository 
3. Copy the file `apr-generator-plugin/access_sheets.py`
4. Paste the file into the folder `SheetShuttle/plugins`
5. (Optional) rename the file to something like `APR-Generator.py`. We'll decide on an official name later
6. Copy the folder `apr-generator-plugin/config`
7. Delete the folder `SheetShuttle/config`
8. Paste the folder from Step 4 in `SheetShuttle/`
9. Change directory in powershell to `SheetShuttle/`
    - The command in step 8 definitely works in powershell, not tested in cmd
10. Run command `sheetshuttle -pn APR-Generator`
    - `pip` install dependencies as needed
