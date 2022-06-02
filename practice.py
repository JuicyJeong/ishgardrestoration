import pandas as pd
import matplotlib.pyplot as plt

# 필요한 데이터를 1위, 12위, 100위 랭크만

df_rank = pd.DataFrame(columns=['Day_Number','World','Job','Points',"Rank","Name"])

for day_number in range(1,11):

    gbs3 = pd.read_csv("DataPreprocessing/GlobalServer/Season3/GB_Season3_Day"+str(day_number)+".csv")
    gbs3 = gbs3.drop(columns="Unnamed: 0")
    gbs3 = gbs3.drop(columns="Name")


    # rank1 = gbs3.loc[gbs3["Rank"]==1]
    # rank12 = gbs3.loc[gbs3["Rank"]==12]
    # rank100 = gbs3.loc[gbs3["Rank"]==100]



    df_rank = pd.concat([df_rank,gbs3],ignore_index=True)
    print(df_rank)
    print(day_number,"일차 데이터 필터링 완료.")

df_rank.to_csv("RankFiltering/GBS3_total.csv")
