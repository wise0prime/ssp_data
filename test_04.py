first = int(input(" 정수1"))
second = int(input(" 정수2"))
third = int(input(" 정수3"))

sumnum= first + second + third

print(f"{first}와 {second}와 {third}의 합은 {sumnum:,}이다.")

#정수를 세번 입력받아 출력하는 코드 테스트였습니다. 
#int로 입력 받을 땐 한 줄코드로 각 각 데이터를 입력받기 위해서는  제 생각에 map함수를 적용하면 되었는데 
#기본 강의에서는 각각 정수를 입력받아 합을 계산하는 간단한 식으로 작성하였습니다. 
#f- string 사용시 {,} 의 사용은 1000단위를 세자리로 끊어주는 기능입니다. 

