import datefinder
import datetime

string1 = "03rd-7th October 2022"
new_string = string1.split('-')
new_list = [p.strip() for p in new_string]
print(new_list[1])
# dddd = " to ".join(new_list)
# # print(dddd)
# matches = datefinder.find_dates(string1)
# for match in matches:
#     print(match)