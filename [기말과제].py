Calorie_total=0
List=[142/100,55/100,1,22/100,35/100,9/100,1/5,2,31/100,236/100,5/2,109/100,3/2,3,3,330/100,24/10,245/100]

select=0
Gram=0
print("추가할 식재료를 선택하세요. 없을시 -1 입력하세요")
print("----------------------------------------------------------------------")
print(" 1)사과      2)포도     3)바나나  4)파   5)양파    6)오이 ")
print(" 7)파프리카   8)샐러드팩  9)양배추  10)돼지고기   11)소고기   12)닭가슴살 ")
print("13)생선     14)계란    15)밥    16)햄 17)베이컨    18)참치 ")
print("----------------------------------------------------------------------")
while select!=-1:
 Gram=0
 select=0
 print(end="재료 번호 입력 : ")
 select=int(input())
 if select==-1:
   break
 else:
   number= select-1
   print(end = "재료의 그람 수를 입력해주세요 : ")
   Gram=int(input())
   Calorie_total+=Gram*List[number]
   print(Gram*List[number], "칼로리가 추가 되었습니다")
   print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("음식 이름은 무엇으로 하시겠습니까?")
title=input()
print(title,"의 칼로리는 ",Calorie_total,"kcal 입니다")
 
 





 



