from access_sheets import run
from Sample_Data_Structure import Students
import sys

data = Students

i = 0
k = 0
for p_id, p_info in data.items():
    if p_id == "Superuser":
        for key in p_info:
            if key == "Total":
                k = p_info.get(key,0)
                print(k)
    else:

    #print("\nPerson ID:", p_id)


        for key in p_info:
        #print(f"{key}: " + f"{p_info[key]}")
            if key == "Total":
                total_value = p_info.get(key,0)
                if total_value/k < .7:
                    apr = "You are dumb"
                    print(apr)
                #print(total_value)
