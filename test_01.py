number = int(input("정수를 입력하세요"))

bi = bin(number)
octa = oct(number)
hexa = hex(number)

print("입력 값의 2진수는 {}, 8진수는 {}, 16진수는{}입니다.".format(bi,octa,hexa))

#p32에 나오는 비트 연산자 관련 테스트 입니다.
#입력값을 받아 진법 함수를 각각 적용해서 출력하는 문제였습니다. 
#정수 12를 입력했을 때 2진수 0b1100 8진수 0o14 16진수 0xc가 나오게 작성합니다. 
