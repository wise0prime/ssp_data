iv_score = int(input(" 면접점수::"))
wr_score= int(input(" 필기점수::"))

grade = " "

if iv_score >= 90 and wr_score >= 90:
    grade = "A"     #print("A 등급")

elif wr_score >=80 and wr_score >=80:

    grade = "B"     #print("B 등급")

elif wr_score >=70 and wr_score >70:

    grade = "C"     #print("C 등급")
else:
    grade = "불합격"     #print("C 등급")

print("{}등급 ".format(grade))
