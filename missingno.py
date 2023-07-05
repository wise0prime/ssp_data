import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

data_nan ={결측치가 있는 데이터}


#데이터 프레임 생성
data_missingno = pd.DataFrame(data = data_nan)


#맷플롯립으로 시각화 생성
plt.rcParams['figure.dpi'] =40


#행렬을 시각화한 데이터프레임 생성
plt.figure(figsize =(8.8), dpi=50)
msno.matrix(df=data_nan)
plt.show()

#행 = 샘플데이터의 수 / 열= 데이터프레임의 모습이 배치됨
#빈 공간이 결측치로 나타난다.

#bar차트를 통한 결측치확인
msno.bar(df=data_nan)
plt.show()

#좌측과 우측의 y값으로 구분되며 좌측은 데이터의 퍼센테이지
#우측은 샘플의 갯수를 의미하며
#최상단의 숫자값은 데이터의 숫자를 보여준다.
