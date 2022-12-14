# # import pandas as pd
# # import numpy as np
# #
# # df_dict = {'CUSTID': ['98981', '897892','32323','98900','98981'], 'CamapignID': ['C1', 'C2','C3','C1', 'C1'],'Units Puchased':[2,1,7,4,2]}
# # campaign_df = pd.DataFrame(data=df_dict)
# # campaign_df
# # print(campaign_df)
# # av_column=campaign_df.[Units Puchased].max()
# # print(av_column)
# # av_row = campaign_df.mean(axis=1)
# # print(av_row)
# a=[]
# name = str(input("enter employee name :"))
# skill = str(input("Skills :"))
# csalary = int(input("enter current salary :"))
# esalary = int(input("enter expected salary :"))
# exp = int(input("enter total year of experience :"))
# if name.isalpha() and skill.isalpha():
#     print(name)
# word = (skill.split(','))
# for i in word:
#     a.append(i)
# for j in a:
#     if j == "sql" or j == "python" or j == "datawarehousing":
#         print("canditate is eligible for this job ")
#     else:
#         print("canditate not eligible for this job")
#     if (csalary >= 5):
#         print("canditate is eligible for this job")
#     else:
#         print("canditate not eligible for this job")
#     if (esalary <= 8):
#         print("canditate is eligible for this job")
#     else:
#         print("canditate not eligible for this job")
#     if (exp >= 5):
#         print("canditate is eligible for this job")
#     else:
#         print("canditate not eligible for this job")


# value=(input("Enter name of city and  Enter name if state : "))
# # item=value.split(",")
# for x in value :
#     item = value.split(",")
#     print(item)
# print("city = ")
# print("State =")
#
# my_string =(input("Enter name of city and  Enter name if state : "))
# a = set(my_string.split(','))
# print(a)

# for item in value:
#     print("city and state\n",item)


# value=(input("Enter name of city and  Enter name if state : "))
# i=tuple(value.split(","))
# print("city = ",i[0])
# print("State =",i[1])

# substring = "code"
# string = "welcome to freecodecamp"
# print(substring in string)

# substring = "zz"
# string = "hello world"
# print(string.find(substring))


string = "welcome to freecodecamp ,platform"
print(string.split(','))
