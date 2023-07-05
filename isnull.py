import pandas as pd

df = pd.read_csv('파일경로',옵션)

print(df.isnull())

#print(df.isnull().sum(axis=0))
#sum과 함께 사용하면 참의 합을 구한다. axis가 참을 반환하여준다.
#결측값이 있는 행과 열을 제거할 땐 df.dropna() 또는 df.dropna(axis=0)을 사용하고
#axis값에 1은 열제거, 0은 행제거이다.
#또한 결측값을 채우기 위해서는 df.fillna()를 사용한다.
#앞 행값으로 채울 때 df.fillna(method='ffill') or df.fillna(method='pad')
#뒷 행의 값으로 채울 때df.fillna(method='bfill') or df.fillna(method='backfill' )
#각 열의 평균값으로 채울때 df.fillna(df.mean())
