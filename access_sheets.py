from sheetshuttle import sheet_collector
import pandas as pd


def run(sheets_keys_file, sheets_config_directory, gh_config_directory, **kwargs):
    """Standard run function."""
    print("hello from the default plugin")
    print("Additional arguments")
    print(kwargs["args"])
