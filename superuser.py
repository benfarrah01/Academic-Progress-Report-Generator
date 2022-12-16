from Sample_Data_Structure import Students
import sys

data = Students

def compare_stu_super(total_value):
    k = 0
    for p_id, p_info in data.items():
        if p_id == "Superuser":
            for key in p_info:
                if key == "Total":
                    k = p_info.get(key,0)
    if total_value/k < .7:
        return True
    else:
        return False
