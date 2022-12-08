from access_sheets import run
from Sample_Data_Structure import Students
import sys

data = Students
print(data)
superuser = data['Student_1']['total']

print(superuser)
print(data['Student_1'].keys())

for p_id, p_info in data.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(f"{key}: " + f"{p_info[key]}")
    # for key[3] in data:
    #     print(key[3])

# for y in i:
#     for i in data[y]:
#         print(i)
# def compare_to_super_user(data):
#     apr = "You need to do better"
#     for key in data:
#         for i in key:
#             i += (i+1)
#             superuser = data[4]
#             if i/superuser > .7:
#                 return apr
