# apr-generator-plugin

## Team 0NE Members
Makell Logan : https://github.com/Makell-Logan
Bergas Anargya : https://github.com/bergasanargya
Ben Farrah : https://github.com/benfarrah01
Darius Googe : https://github.com/Darius90332
Luke Barker

## Description
This is a plugin created by team 0NE for sheetshuttle. At our client's request we created a plugin to gather data from a google sheet containing a Professor's gradebook. Our program sorts through that data, figuring out which students aren't doing well (If their overall grade is less than a 70%) then write a Academic Progress Report, that gives them a warning, telling them how many days they've missed and what assignments they didn't do well on (Received a score less than 60%), encouraging them to reach out to the Professor and see what they can do to improve their grade. It then sends out that report as a email to the student and their advisor. 

In order to make this possible we used:
- Python
- SheetShuttle
- The Google Sheets API
- The Gmail API

These are some challenges we faced, while designing this plugin:
- We struggled with converting the google sheet into a dictionary that we could access in our `APR-generator.py` as we didn't have much experience with it.
- We had never used the Gmail API, so that we had to research and learn about it first before we could implement it.
- We never used Mkdocs before, so we had trouble getting the docstings onto the web pages.

## How To Use Our Plugin
1. Copy the file `apr-generator-plugin/access_sheets.py`
2. Paste the file into the folder `SheetShuttle/plugins`
3. (Optional) rename the file to something like `APR-Generator.py`. We'll decide on an official name later
4. Copy the folder `apr-generator-plugin/config`
5. Delete the folder `SheetShuttle/config`
6. Paste the folder from Step 4 in `SheetShuttle/`
7. Change directory in powershell to `SheetShuttle/`
    - The command in step 8 definitely works in powershell, not tested in cmd
8. Run command `sheetshuttle -pn APR-Generator`
    - `pip` install dependencies as needed


## Tests

