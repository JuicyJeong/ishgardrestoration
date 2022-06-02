import requests
import pandas as pd
import json
import time

#글로벌  선언
save_df = pd.DataFrame(columns=['Day_Number','World','Job','Points',"Rank","Name"])
server_list = ["carbuncle","chocobo",'moogle',"tonberry"]
job_list = ['crp','bsm','arm','gsm','ltw', 'wvr', 'alc', 'cul', 'min', 'btn', 'fsh']
loop_number = 0
temp_job_name = "tempjob"
#글로벌 선언

for season_loop in range(3,5): #시즌 2는 따로 돌리자. day 3부터 있어서 조건문 처리 따로 나중에.
    for day_loop in range(1,11):

        common_path = "RawData/KRServer/KRJSON/Season"
        save_path =common_path +str(season_loop)+"/"+"Day"+str(day_loop)+".json"
        temp = open(save_path)
        json1_str = temp.read()
        temp_json = json.loads(json1_str) #temp_json은 for문 사이에서 돌리면서 돌아가는 json 파일
        ''
        ##json에 있는 정보: 유저네임, 점수, 랭크(는 내가 따로 만들기), 서버, 직업
        ## temp_json[server_loop][job_loop][순위(0:99)][0:name,1:점수]
        for server_loop in server_list:
            for job_loop in job_list:
                rank_len = len(temp_json[server_loop][job_loop])
                rank_counter = 0 #랭크 초기화
                while rank_len > rank_counter: #1위부터 100위, 시즌3은 200위까지 돌게하는 루프

                    name_loop = temp_json[server_loop][job_loop][rank_counter][0]
                    point_loop = temp_json[server_loop][job_loop][rank_counter][1]

                    list_data = [day_loop,server_loop,job_loop,point_loop,'NaN',name_loop] #빈 데이터프레임에 열을 추가하는 방식
                    save_df = save_df.append(pd.Series(list_data, index=save_df.columns), ignore_index=True)
                    rank_counter = rank_counter+1

                print(save_df.tail())
                print(save_df.head)
                time.sleep(0.1)

        #랭크 매기기
        day_len = len(save_df)
        print(day_len)
        while loop_number < day_len:
            if temp_job_name == save_df["Job"].loc[loop_number]:
                pass
            else:
                temp_rank_number = 1
                temp_job_name = save_df["Job"].loc[loop_number]

            save_df["Rank"].loc[loop_number] = temp_rank_number
            temp_rank_number += 1
            loop_number += 1

        #루프 변수 한번 초기화 시켜서 다시 돌려주기#
        temp_job_name = "tempjob"
        loop_number = 0
        #루프 변수 한번 초기화 시켜서 다시 돌려주기#

        #랭크 매기기

        #직업 대문자로 변환
        save_df["Job"] = save_df["Job"].str.upper()

        #파일 저장
        save_path = ("DataPreprocessing/KRServer/Season")
        save_df.to_csv(save_path + str(season_loop)+"/KR_Season" + str(season_loop) + "_Day"+ str(day_loop) + ".csv")
        save_df = pd.DataFrame(columns=['Day_Number', 'World', 'Job', 'Points', "Rank", "Name"])
        time.sleep(1)


