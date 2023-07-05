import pandas as pd

df = pd.read_csv('파일경로',옵션)

print(df.info)

#작업할 csv파일을 파이썬으로 불러와 판다스를 이용하여 데이터프레임을 만든 후
#데이터를 살펴 볼 때 사용하는 메서드이다
#info()메서드는 데이터 프레임에 관한 기본 정보를 화면에 출력한다.
#dataframe 객체.info()
