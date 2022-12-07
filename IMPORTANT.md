# ATTENTION:

## In order to get this plugin to work, you must:

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

NOTE: if you don't want to move the python file, you can cd to `SheetShuttle/` and run the command `sheetshuttle -pd 'C:\School(c-drive)\cmpsc\Repositories\203\apr-generator-plugin' -pn access_sheets`
    - You must already have the key file in `/SheetShuttle` and have completed steps 4-6.