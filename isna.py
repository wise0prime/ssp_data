~생략

df = pd.DataFrame([샘플데이터])

print(df.isna())
#sum()과 함게 사용하여 갯수확인을 할 수 있다.

#넘파이와 다르게 숫자, 글자 , nan값 뿐 아니라 시리즈와 데이터프레임도
#변수로 받을 수 있다.
#특정 열의 NaN값을 찾을 때 df[df.column.isna( )]
