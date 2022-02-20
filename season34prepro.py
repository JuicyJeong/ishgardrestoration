import numpy as np
import pandas as pd
import os
import time

# for문으로 하나씩 스캔할때 사용. 테스트할때 너무 양이 많으면 range값 수정하자.
season_range = list(range(3,5))
day_range = list(range(1,11))

# print(day_range)
# print(season_range)

#초기 데이터프레임을 만들고 여기에 어팬드하는 방식으로 day별 데이터프레임을 저장하기
save_df = pd.DataFrame(columns=['Day_Number','World','Job','Points',"Rank","Name"])

for temp_season_number in season_range:

    for temp_day_number in day_range:
        dir_path = "season"+str(temp_season_number)+"/day"+str(temp_day_number)+"/"
        csv_list = os.listdir(dir_path) #폴더에 있는 파일들을 읽어오기 #day별로 나뉘어져 있음. day를 변수로 바꿔야함.
        csv_list.sort() #오름차순 정렬
        del csv_list[0]
        # print(csv_list) ### 월드_직업명으로 되어있는 리스트
        #  #하나 콜해서 전처리를 먼저 시켜놓자.

        for csv_path in csv_list:
            csv_file_name = dir_path + csv_path
            temp_df = pd.read_csv(csv_file_name)

            # print(csv_file_name)
            # print(temp_df.head())

            ######전처리 구역######
            #파일 1차 drop 돌리고 append 하는게 데이터 붙이는데 좀 더 절약해서 붙이는게 나을듯?
            #확인해보면 world, job이 이름이 아니라 ID값으로 되어있음. for 문에서 돌리고 있는 로컬변수를 칼럼 값에 replace하기.
            #컬럼명을 2차의 변수명과 동일하게 변경. 컬럼순서도 재배치하기. =>> 해결!
            #day값 추가하기

            #데이터프레임 전처리 과정
            temp_df = temp_df.drop(["id","yesterdayRank","yesterdayScore",'iconUrl'],axis=1) #안쓸 칼럼 드랍
            temp_df['Day_Number'] = temp_day_number # 여기 변수 처리해야함. >> 처리 완료!
            #이름 양식이랑 순서 맞추기
            temp_df.rename(columns={'worldId':'World','jobId':'Job','rank':'Rank','name':"Name",'score':'Points','change':'Change'},inplace = True)
            temp_df = temp_df[['Day_Number','World','Job','Points',"Rank","Name"]]
            ###World Job ID를 이름으로 변경
            worldJob_arr = csv_path.split("_")#csv에 있는 값을 스플릿해서 월드, 직업으로 리스트로 뽑아두기
            world_str = worldJob_arr[0]
            job_str = worldJob_arr[1][:-4]

            temp_world_id = temp_df["World"][0] #월드 int값을 저장
            temp_job_id = temp_df["Job"][0] #잡 인트 값을 저장

            temp_df.loc[temp_df['World'] == temp_world_id, 'World'] = world_str #현재 돌아가는 월드, 잡으로 변경
            temp_df.loc[temp_df["Job"] == temp_job_id, "Job"] = job_str

            #초기값에 저장하고 계속 리스트 돌떄마다 하나씩 추가하기.
            if len(save_df) == 0:
                save_df = pd.concat([save_df, temp_df])
            else:
                save_df = pd.concat([save_df,temp_df])
            print(csv_file_name)
            print(temp_df.head())
        #빠져나와서 인데스 재정령하고 저장하기. 샘플이 아니라 이제부터
        save_df.reset_index(drop=True,inplace=True)
        prepro34_path = "dataprepro34"+ "/" + "season" + str(temp_season_number)+"/" #저장은 이제 데이별로 폴더를 안만들어도 되잖아
        prepro34_file_name = "prepro" +"season"+str(temp_season_number) + "day"+str(temp_day_number)+".csv"
        # print(prepro34_file_name)
        save_df.to_csv(prepro34_path+prepro34_file_name)
        #마지막에 한번더 초기화 선언 해줘서 day넘어갈때마다 누적되는거 한번 초기화 시켜주기
        save_df = pd.DataFrame(columns=['Day_Number', 'World', 'Job', 'Points', "Rank", "Name"])
