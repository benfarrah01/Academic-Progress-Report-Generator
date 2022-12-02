""""This file, when put into `SheetShuttle/plugins`, can be run to display the contents of the sheet."""
from sheetshuttle import sheet_collector
#from sheetshuttle import Sheet

# File containing authentication information. DON'T PUSH `new_key.json` TO GITHUB!!!
key_file='new_key.json'
# Directory containing config information for our google sheet
sources_dir='config/sheet_sources'

def run(sheets_keys_file, sheets_config_directory, **kwargs):
    """Example run function. Collect and display info from google sheet."""
    # Create SheetCollector object named `my_collector`
    #   Created with args `key_file` and `sources_dir`
    my_collector = sheet_collector.SheetCollector(key_file, sources_dir)
    my_collector.collect_files()
    # Display contents of the sheet
    my_collector.print_contents()

    #my_sheet = sheet_collector.Sheet()
