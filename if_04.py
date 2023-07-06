password = input("패스워드입력::")
scode= input("학교코드입력::")

if scode == "hankook":
    if password == "hk1234":
          print("로그인성공!")

    else:
        print("패스워드 오류")

else:
       print("학교코드 오류")


# if중첩과 else를 통해 입력값을 받아 중첩조건을 완성하는 진단문제입니다. p55참조
