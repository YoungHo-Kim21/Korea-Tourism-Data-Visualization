#방한 외래관광객 월별 heatmap그래프 그리기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#index : year(연도)행으로 DF불러오기
data = pd.read_csv("/content/Foreigner_Korea_monthly.csv", index_col=0)
#최근 10년 자료만 불러와서 numpy배열로 바꾸기, 1000으로 나눠서 천 단위 수치로 만들기
data_m1 = data.tail(10).to_numpy(dtype=float)/1000

#인덱스(행)에 연도 추가, 열에 월 추가해서 새로운 DF만들기
row_ = list(range(2015,2025))
col_ = ['Jan','Feb',"Mar","Apr",'May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
data_m2 = pd.DataFrame(data_m1,index=row_,columns=col_)

import seaborn as sns
#plt크기 36*20으로 정함
plt.figure(figsize=(36,20))
#heatmap생성 : 사각형 안의 숫자 크기를 20으로, 숫자 포맷을 소수점 1자리까지, label을 천명으로 표기
sns.heatmap(data_m2, annot=True,annot_kws={"size":20},fmt=".1f",
            cmap='Blues',cbar_kws={'label':'천 명'})
#타이틀 생성 : 최근 10년간 방한 외국인 통계(단위 : 천명)
plt.title('Statistics on foreign visitors to Korea over the past 10 years (unit: thousands)\n', fontsize=40)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.show()
#heatmap을 png파일로 저장.
plt.savefig("heatmap_recent10years_monthly.png", dpi=300)
