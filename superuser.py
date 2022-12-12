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
<<<<<<< HEAD
=======

def compare_stu_super(super_user, user):
    score = user / super_user
    if score <= .7:
        return True 
    elif score >= .7:
        return False
    return score




        #i += 1
        #if i >= 1:
            #break

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
>>>>>>> 4ab82a674b311bb1c63112d4747d427cd78292b1
