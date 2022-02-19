import numpy as np
import pandas as pd
import os
import time

csv_list = os.listdir("season3/day1") #폴더에 있는 파일들을 읽어오기 #day별로 나뉘어져 있음. day를 변수로 바꿔야함.
csv_list.sort() #오름차순 정렬
del csv_list[0]
print(csv_list)