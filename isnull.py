import pandas as pd

df = pd.read_csv('파일경로',옵션)

print(df.isnull())

#print(df.isnull().sum(axis=0))
#sum과 함께 사용하면 참의 합을 구한다. axis가 참을 반환하여준다.
