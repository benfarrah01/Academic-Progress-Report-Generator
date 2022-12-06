from access_sheets import run
from APR_Generator import apr_generator
from Sample_Data_Structure import Students

def compare_to_super_user():
    apr = "You need to do better"
    data = Students
    for row in data:
        for i in row:
            i += (i+1)
            superuser = data[1]
            if i/superuser > .7:
                return apr
