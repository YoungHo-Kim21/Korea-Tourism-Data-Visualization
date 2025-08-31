import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#방한 외국인 및 국민 해외관광객 수 csv데이터 DF로 가져오기(인덱스는 0열(Year)로 설정)
data_in = pd.read_csv("/content/Foreigner_Korea_monthly.csv", index_col=0)
data_out = pd.read_csv("/content/Koreans_abroad_monthly.csv", index_col=0)
#각각 DF에 해당 연도 총 관광객 수를 Total열로 만들고 1,000으로 나누기.
data_in['Total'] = data_in.iloc[25:,0:12].sum(axis=1)/1000
data_out['Total'] = data_out.iloc[25:,0:12].sum(axis=1)/1000

#data_in DF(방한 외국인 DF)에서 인덱스(연도,Year열)의 데이터를 가져오기
x = data_in.index

#그림의 사이즈를 16*9로 설정
fig, ax1 = plt.subplots(figsize=(16,9))

#2번째 축 설정
ax2 = ax1.twinx()

#1번째 축의 그래프 : 국민 해외관광객 대비 방한 외국인 비율, 불투명도 30% bar차트로 나타내기.
ratio = data_in['Total']/data_out['Total']
ax1.bar(x,ratio,alpha=0.3,color='#66eeee')

#2번째 축(메인)의 그래프 : 방한 외국인 수와 국민 해외관광객 수를 천명 단위로 선 그래프로 색을 달리하여 그리기
ax2.plot(x,data_in['Total'],color='#11bb11',linewidth=2,label='Inbound to Korea')
ax2.plot(x,data_out['Total'],color='#1111bb',linewidth=2,label='Outbound from Korea')

#축 폰트 크기 조절
ax1.tick_params(labelsize=12)
ax2.tick_params(axis='y', labelsize=12)

#차트 제목 : 한국 방문/한국인의 해외 방문에 대한 그래프(단위 : 천명)
plt.title('Statistics on Inbound to/Outbound from Korea(unit:thousands)\n',fontsize=20)

#격자와 범례 설정
plt.grid(True)
plt.legend(fontsize=12)

#plt.show()
#그래프들을 png파일로 저장
plt.savefig("chart_inbound_outbound_Korea.png", dpi=300)
