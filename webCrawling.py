import requests
import pandas as pd
import json
import time
#https://lalachievements.com << api를 지원하여 json 데이터로 파일을 읽을 수 있음. 웹크롤링으로 긁어오기

####월드 리스트, 직업 리스트로 미리 선언해두기, 갖고 있는 텍스트 파일에서 뽑아와서 리스트에 넣기.
jobs_worlds = ["listWorldJob/jobs.txt",'listWorldJob/worlds.txt']
for path in jobs_worlds:

    filepath =path

    with open(filepath) as f:
        lines = f.readlines()

    lines = [line.rstrip('\n') for line in lines]
    #print(path[13:-5],'의 변수: ',lines)

    if path[13:-5] == 'job': #### 여기 좀 더 변수선언부를 잘 만들고 싶은데 제대로 생각이 안떠오름
        job = lines
    else:
        world = lines
##변수 잘 입력 되었는지 확인하기.
print(job)
print(world)

#job변수와 world 변수와 range[3,4](3차,4차용) range[1,10](1일차~10일차) 로 df를 만들고 추가될때마다 밑에 어팬드 하는 방식으로 만들자
# 파일 형식: https://lalachievements.com/api/ranking/ishgard/서버/시즌/직업/일자
# 돌릴때마다 콜해와서 저장하면 서버가 울지도 모르니까 api로 땡기는건 한번만 해갖고 와서 먼저 저장을 해두기.
common_url = "https://lalachievements.com/api/ranking/ishgard/"
# season_range = range(3,)
temp_list = ['Adamantoise', 'Aegis', 'Alexander', 'Anima', 'Asura', 'Atomos', 'Bahamut', 'Balmung', 'Behemoth', 'Belias', 'Brynhildr', 'Cactuar', 'Carbuncle', 'Cerberus', 'Chocobo', 'Coeurl', 'Diabolos', 'Durandal', 'Excalibur', 'Exodus', 'Faerie', 'Famfrit', 'Fenrir', 'Garuda', 'Gilgamesh', 'Goblin', 'Gungnir', 'Hades', 'Hyperion', 'Ifrit', 'Ixion', 'Jenova', 'Kujata', 'Lamia', 'Leviathan', 'Lich', 'Louisoix', 'Malboro', 'Mandragora', 'Masamune', 'Mateus', 'Midgardsormr', 'Moogle', 'Odin', 'Omega', 'Pandaemonium',]
for season_loop in range(3,5):
    for day_loop in range(1,11):
        for world_loop in world:

            if season_loop == 3 and day_loop == 1 and world_loop in temp_list:
                continue
            for job_loop in job:

                call_url = common_url+world_loop+"/"+str(season_loop)+'/'+job_loop+'/'+str(day_loop)
                # url = requests.get("https://lalachievements.com/api/ranking/ishgard/Aegis/3/BSM/2")
                url = requests.get(call_url)
                text = url.text
                # print(text)
                info = json.loads(text)
                df = pd.json_normalize(info['chars'])
                # print(df.head())
                call_csv_path = "season"+str(season_loop)+"/"+"day"+str(day_loop)+"/"+world_loop+"_"+job_loop+".csv"
                df.to_csv(call_csv_path)
                print(call_csv_path+"저장완료.")
                time.sleep(0.9)




######전처리 구역######
#파일 1차 drop 돌리고 append 하는게 데이터 붙이는데 좀 더 절약해서 붙이는게 나을듯?
#확인해보면 world, job이 이름이 아니라 ID값으로 되어있음. for 문에서 돌리고 있는 로컬변수를 칼럼 값에 replace하기.
#컬럼명을 2차의 변수명과 동일하게 변경. 컬럼순서도 재배치하기.
#day값 추가하기


# df = df.drop(["id","yesterdayRank","yesterdayScore",'iconUrl'],axis=1)
# df['Day_Number'] = 1 # 여기 변수 처리해야함.
# df.rename(columns={'worldId':'World','jobId':'Job','rank':'Rank','name':"Name",'score':'Points','change':'Change'},inplace = True)
# df = df[['Day_Number','World','Job','Points',"Rank","Name"]]
# print(df.head())

# df.to_csv("samplecsv.csv")

