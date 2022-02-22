import requests
import pandas as pd
import json
import time

'''
##################################NOTICE##########################################
콜해오는 URL 기본 양식>>
https://home.idyllshi.re/ishresto/data/[s3:s4]/[day1:day10].json
****** 시즌2는 데이터가 3일차부터 있으니 루프 돌릴때 참고하기*****

루프 돌려야 하는 부분은 시즌, 날짜 두개. df에 저장하고 파일 유형 확인하기.

돌릴때마다 콜해와서 저장하면 서버가 울지도 모르니까 api로 땡기는건 한번만 해갖고 와서 먼저 저장을 해두기.
##################################NOTICE##########################################
'''

common_url = "https://home.idyllshi.re/ishresto/data/"

for season_loop in range(4,5):
    for day_loop in range(1,11):

        call_url = common_url+"s"+str(season_loop)+"/day"+str(day_loop)+".json"
        url = requests.get(call_url)
        text = url.text
        # print(text)
        info = json.loads(text)

        #저장 경로 설정
        common_path = "RawData/KRServer/KRJSON/Season"
        save_path =common_path +str(season_loop)+"/"+"Day"+str(day_loop)+".json"

        #저장(인코딩 설정)
        with open(save_path, "w",encoding="UTF-8") as f:
            json.dump(info, f, ensure_ascii=False)
        print(save_path+" 저장완료")
        time.sleep(2)

        # print(df.head())








