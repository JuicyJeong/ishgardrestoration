import numpy as np
import pandas as pd
import os
import time
#version_check
# print(np.__version__)
# print(pd.__version__)
#----------------------------------#

csv_list = os.listdir("RawData/GlobalServer/GBseason2/reddit/") #original 폴더에 있는 파일들을 읽어오기
csv_list.sort() #오름차순 정렬

######지역변수 선언########
csv_list_loop =0
real_csv = []
csv_listnumber = len(csv_list)
######지역변수 선언######

#csv 파일명 반복문 돌려서 리스트에 저장해두기(경로 포함)
csv_listnumber = len(csv_list)

while csv_list_loop < csv_listnumber:
    real_csv.append("RawData/GlobalServer/GBseason2/reddit/"+ csv_list[csv_list_loop])
    csv_list_loop += 1
print(real_csv)

csv_range = range(0,len(real_csv))
print(csv_range)


### i 는 전체 for문에서 돌리는 반복 변수
for i in csv_range:
    # file import #나중에 파일 경로 수정하는걸로 하자
    dayN_data = pd.read_csv(real_csv[i])
    print(dayN_data.head()) #데이터 프레임 확인.

    #럼럼 전처리구역: 칼럼에 값 추가, 컬럼 대소문자 변경
    dayN_data = dayN_data.drop(["DC"], axis=1)
    dayN_data["Day_Number"] = i+1 #여기 변수처리 필요
    dayN_data["Rank"] = 1
    dayN_data.rename(columns={'world': 'World'},inplace=True)
    dayN_data = dayN_data[['Day_Number', 'World', 'Job', 'Points', "Rank", "Name"]]

    #임시변수 선언구역######
    temp_rank_number = 1
    temp_job_name = "tempjob"
    loop_number = 0
    temp_tuple = ('server','job')
    temp_dic = dict()
    print_time = time.time() #현재시간 호출, 일정시간간격마다 진행상황 확인하기 위한 While문 안쪽에서 확인하기.

    #job 변수 선언 하고 for문으로 돌려버리기

    day_len = len(dayN_data)
    print(day_len)
    while loop_number < day_len:
        if temp_job_name == dayN_data["Job"].loc[loop_number]:
            pass
        else:
            temp_rank_number = 1
            temp_job_name = dayN_data["Job"].loc[loop_number]

        dayN_data["Rank"].loc[loop_number] =temp_rank_number
        temp_rank_number += 1
        loop_number += 1

        ##현재 진행상황을 확인하게 하는 구간
        print_time_while = time.time()
        if print_time + 3 < print_time_while:
            print("현재 ", i + 1, "일차", loop_number, "번째 스캔중!")
            print_time = print_time_while
        ##현재 진행상황을 확인하게 하는 구간


    print(dayN_data.head(20)) #데이터 프레임 확인.
    dayN_data.to_csv("DataPreprocessing/GlobalServer/Season2/GB_Season2_Day{0}.csv".format(i+1)) #여기도 리스트로 반환#