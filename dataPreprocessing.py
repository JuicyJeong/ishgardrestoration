import numpy as np
import pandas as pd

#version_check
# print(np.__version__)
# print(pd.__version__)

#----------------------------------#

#file import #나중에 파일 경로 수정하는걸로 하자
day1_data = pd.read_csv("points_2020-03-12.csv")
# print(day1_data.head()) #데이터 프레임 확인.

#데이터 전처리.
# day1_data = day1_data.drop(["Empty_2"],axis=1)
day1_data["Day_Number"] = 1
day1_data["Rank"] = 1

temp_rank_number = 1
temp_job_name = "tempjob"
loop_number = 0
#job 변수 선언 하고 for문으로 돌려버리기

#Rank 끝까지 훑는동안 1-100까지 랭크 맞게 입력하기. job 변수 스캔하면서 같으면 += 1, 다르면 그 변수를 넣고 다시 1부터 시작.

print(len(day1_data))

# print("직업이름" + day1_data["Job"].loc[12345])

while loop_number <= len(day1_data):
    if temp_job_name == day1_data["Job"][loop_number]:
        day1_data["Rank"].loc[loop_number] = temp_rank_number
        temp_rank_number += 1
    else:
        temp_job_name = day1_data["Job"].loc[loop_number]
        temp_rank_number = 1




# for i in day1_data['Job']:
#     if temp_job_name ==
#     day1_data["Rank"] = temp_rank_number
#     temp_rank_number += 1




print(day1_data.head(15)) #데이터 프레임 확인.

