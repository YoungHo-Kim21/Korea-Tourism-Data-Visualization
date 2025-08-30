import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#공공데이터포털에서 국민 해외관광객 통계 DF로 만들기
statistics = pd.read_excel("/content/sta_travelKorea.xlsx",sheet_name='국민 해외관광객')

#numpy배열로 만들어서 1~4행 결측값 제거
new_ar = np.array(statistics.iloc[5:55,0])
indnum = range(3,15)
for i in indnum:
  ar = np.array(statistics.iloc[5:55,i])
  new_ar = np.vstack([new_ar,ar])
#new_ar 배열(행:월, 열:연도)

#열 이름 만들어주기
col = ['Year']+list(range(1,13))

#새로운 df 생성, 인덱스(행) : 연도, 열 : 월
data = pd.DataFrame(new_ar.T, columns=col)
data.set_index('Year',inplace=True)

#csv파일로 저장
data.to_csv('Koreans_abroad_monthly.csv')
