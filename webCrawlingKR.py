import requests
import pandas as pd
import json
import time

#https://home.idyllshi.re/ishresto/data/[s3:s4]/[day1:day10].json
#****** 시즌2는 데이터가 3일차부터 있으니 루프 돌릴때 참고하기*****

#루프 돌려야 하는 부분은 시즌, 날짜 두개. df에 저장하고 파일 유형 확인하기.

#job변수와 world 변수와 range[3,4](3차,4차용) range[1,10](1일차~10일차) 로 df를 만들고 추가될때마다 밑에 어팬드 하는 방식으로 만들자

# 파일 형식: https://lalachievements.com/api/ranking/ishgard/서버/시즌/직업/일자
# 돌릴때마다 콜해와서 저장하면 서버가 울지도 모르니까 api로 땡기는건 한번만 해갖고 와서 먼저 저장을 해두기.
common_url = "https://home.idyllshi.re/ishresto/data/"
for season_loop in range(3,4):
    for day_loop in range(10,11):

        call_url = common_url+"s"+str(season_loop)+"/day"+str(day_loop)+".json"
        url = requests.get(call_url)
        text = url.text
        # print(text)
        info = json.loads(text)
        df = pd.json_normalize(info)

        df= pd.json_normalize()

        print(df.head())



        # call_csv_path = "season"+str(season_loop)+"/"+"day"+str(day_loop)+"/"+world_loop+"_"+job_loop+".csv"
        df.to_csv("sample.csv")
        # print(call_csv_path+"저장완료.")
        # time.sleep(20)




######전처리 구역######
#파일 1차 drop 돌리고 append 하는게 데이터 붙이는데 좀 더 절약해서 붙이는게 나을듯?
#확인해보면 world, job이 이름이 아니라 ID값으로 되어있음. for 문에서 돌리고 있는 로컬변수를 칼럼 값에 replace하기.
#컬럼명을 2차의 변수명과 동일하게 변경. 컬럼순서도 재배치하기.
#day값 추가하기





