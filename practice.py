'''
from random import *
date = randint(4, 28) #4에서 28까지 랜덤으로 숫자 뽑기

print("오프라인 스터디 모임 날짜는 매월", str(date), "일로 선정되었습니다.")

sentence = """나는 소년이고
파이썬은 쉬워요"""
print(sentence)

jumin = "810525-2009313"

print ("성별 :" + jumin[7]) #2
print ("연 :" + jumin[0:2]) #81
print ("월 :" + jumin[2:4]) #05
print ("일 :" + jumin[4:6]) #25

print ("생년월일 :" + jumin[:6]) #810525
print ("뒤 7자리 :" + jumin[7:]) #2009313
print ("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #2119313

python = "Python is Amazing"
print(python.lower())  # 모든 문자열 소문자로 출력
print(python.upper())  # 모든 문자열 대문자로 출력
print(python[0].isupper()) #첫번째 문자가 대문자인가?
print(len(python)) #문자열의 길이
print (python.replace("Python", "Java")) #문자열 대체

index = python.index("n") #n의 위치 찾기
print(index)
index = python.index("n", index + 1) #앞에서 찾은 위치 그 다음부터 검색, index + 1은 시작 위치
print(index)

print(python.find("Java")) #원하는 문자열이 없을 때 -1 출력
# print(python.index("Java")) #원하는 문자열이 없을 때 프로그램 종료
print("hi")

print(python.count("n"))


print("나는 %d살입니다." %20) #정수
print("나는 %s을 좋아해요" % "파이썬") #문자열
print ("Apple은 %c로 시작해요" % "A") #문자

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))
print ("나는 {}살입니다.".format(20)) #()안에 원하는 값을 넣고 그 값이 {}로 들어간다.
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  #나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) #나는 빨간색과 파란색을 좋아해요.

print("나는 {age}살이며, {color}색을 좋아해요".format(
    age = 20, color = "빨강")) #나는 20살이며, 빨강색을 좋아해요

age = 20
color = "빨간"
#f로 시작하고 실제 중괄호안에 들어가는 값은 실제 변수선언된 값을 갖고 온다.
print(f"나는 {age}살이며, {color}색을 좋아해요")

print ("백문이 불여일견 \n백견이 불여일타")

print ("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

print("C:\\Users\\junghyunchoi\\Desktop\\PythonWorkspace")

print("RED Apple\rPine") #\r 커서를 맨 앞으로 이동
print("Redd\bApple") # \b 백스페이스 (한 글자 삭제)
print("Red\tApple" ) #\t tap



# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예  http://naver.com
# 규칙 1: http://부분은 제외= > naver.com
# 규칙 2: 처음 만나는 점 (.) 이후 부분은 제외=> naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성

# 예) 생성된 비밀번호 : nav51!


url = "http://youtube.com"
my_str = url.replace("http://", "") #규칙 1

my_str = my_str[ :my_str.index(".")] #규칙 2

password = my_str [:3] + str(len(my_str)) + str(my_str.count("e")) + "!" #규칙 3
print("{0}의 비밀번호는 {1} 입니다".format(url,password))

num_list = [1,2,3,4,5]
mix_list = ["Joseho", 20, False]
num_list += mix_list # num_list.extend(mix_list)
print (num_list)



cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.[5]) #프로그램 종료
print(cabinet.get(5) #None 으로 출력
print(cabinet.get(5, "사용 가능"))
print ("hi")

print (3 in cabinet) #True
print (5 in cabinet) #False


cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet ["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print (cabinet)

#간 손님

del cabinet["A-3"]
print (cabinet)

#Key들만 출력
print(cabinet.keys())  # dict_keys(['B-100', 'C-20'])

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕폐점

cabinet.clear()
print(cabinet)



# 튜플
# 튜플에서는 변경, 추가가 불가능하지만 리스트보다 속도가 빠르다. 
# 변경되지 않는 값에 사용 가능
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print (name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
print(name, hobby)


# set (집합)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print (my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 
print (java | python)
print (java.union(python))

#차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹음
java.remove("김태호")
print(java)


#자료구조의 변경
#커피숍
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))



# 퀴즈
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 장석하시오

# 조건 1: 댓글은 20명이 작성하였고 아이디는 1~20이라 가정
# 조건 2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건 3: random모듈의 suffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --


from random import *

users = range(1, 21)
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")


weather = "rain"
if weather == "rain":
    print("please bring an umbrella")
elif weather == "dusty":
    print("please bring a mask")
else:
    print("you dont need to bring anything")


weather = input("hows the weather today?")

if weather == "rain" or weather == "snow":
    print("please bring an umbrella")
elif weather == "dusty":
    print("please bring a mask")
else:
    print("you dont need to bring anything")


temp = int(input("what temperature is today?"))
if temp >= 30:
    print ("Its too hot. dont go out")
elif temp >= 10 and temp < 30:
    print("Its a ok weather")
elif 0 <= temp > 10:
    print("please bring a jacket")
else:
    print("its tooooo cold, dont go out")


#randrange()
for waiting_no in range(1,6): #1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print ("{0}, 커피가 준비되었습니다.".format(customer))


#while
customer = "토르"
index = 5
while index >= 1:
    print ("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")


customer = "torr"
person = "Unknown"

while person != customer:
    print("{0}, coffee is ready.".format(customer))
    person = input("What is your name?") 


absent = [2,5] #결석
no_book  = [7] #책을 깜빡했음
for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지! {0}은 교무실로 따라와".format(student))
        break
    print("{0}아, 책을 읽어주렴".format(student))



#출석번호가 1,2,3,4,5앞에 100을 붙이기로 함 -> 101,102,103,104,105
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] #i에 100을 더한 값을 넣겠다
print(studens)


#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)


#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


# 당신은 cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때,
# 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다
# 조건 2 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2 분

from random import *

cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1에서 50 이라는 수 (승객)
    time = randint(5, 51) # 5분에서 50분 소요 시간
    if 5 <= time <= 15 : #5분에서 15분 이내의 손님 (매칭 성공), 탑승 수 증가 처리
        print("[o]{0} 번째 손님 (소요시간 :{1}분)".format(i,time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ]{0} 번째 손님 (소요시간 :{1}분)".format(i, time))
    
print ("총 탑승 승객 : {0} 분".format(cnt))


def open_account():
    print ("New account is creadted")

# open_account()

def deposit(balance, money): #입금
    print ("Deposited. The balance is {0}.".format(balance + money))
    return balance + money
def withdraw(balance, money):
    if balance >= money: #잔액이 출금보다 많으면
        print("Withdrawal, The balance is {0}.".format(balance - money))
        return balance - money
    else:
        print("You can not withdraw. The balance is {0}.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금할 경우 수수료 발생
    commission = 100 #수수료 100월
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("Commision is {0}, the balance is {1}.".format(commission, balance))
 


def profile(name, age, main_lang):
    print("이름 :{0} \t나이 : {1}\t 주 사용 언어 :{2}" \ 
    .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 같은 학교, 같은 학년, 같은 반, 같은 수업  (기본값)

def profile(name, age=17, main_lang="파이썬"):
    print("이름 :{0} \t나이 : {1}\t 주 사용 언어 :{2}"
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")


def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "파이썬", age =  25, name = "김태호")



def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print ("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    print(lang1, lang2, lang3, lang4, lang5)



def profile(name, age, *language): #가변인자
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#","JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


# 지역변수 : 함수 내에서만 쓸 수 있는 함수 호출될 때 만들어지고 함수 호출 끝나면 사라짐
# 전역변수 : 모든 프로그램 내에서 호출 할 수 있는 변수 (많이 쓰면 코드 관리 어려워짐)

gun = 10


def checkpoint(soldiers):  # 경계근무
    # gun = 20
    global gun  # 전역 공간에 있는 gun을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)  # 두 명이 경계 근무 나감
print("남은 총 : {0}".format(gun))




gun = 10


def checkpoint(soldiers):  # 경계근무
    # gun = 20
    global gun  # 전역 공간에 있는 gun을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 두 명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))



# 퀴즈 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1 :  표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.



# 아래 내가 한건데 소수점은 못했음

gender = input("당신의 성별은 무엇입니까? 남자 또는 여자")
height = input ("당신의 키는 몇 cm 입니까?")

def std_weight(gender, height):
    if gender == "여자":
        weight = round(int(height) / 100 * int(height) / 100 * 21, 2)
        print ("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
    elif gender == "남자":
        weight = round(int(height) / 100 * int(height) / 100 * 22, 2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
    else:
        print("error")
        return

std_weight(gender, height)

# 여기까지가 내가 쓴거!




def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return hiehg * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(weight, gender, weight))



# 표준입출력

print("Python", "Java", sep=" , ", end="?")
print("무엇이 더 재미있을까요?")



import sys
print("Python", "Java", file=sys.stdout) #표준출력로 처리됨
print("Python", "Java", file=sys.stderr)  #표준에러로 처리됨



scores = {"math":0, "english":50 , "coding":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #괄호안의 ,가 :로 처리

# 은행 대기순번표
# 001, 002, 003

for num in range(1,21):
    print ("number : " + str(num).zfill(3))


answer = input("please put anything : ") #input에 입력되는 숫자는 모두 str 처리된다
answer = 10
print(type(answer))
#print ("what you put is " + answer + ".")


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:>10}".format(500)) #500

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0:>+10}".format(300)) # +300
print("{0:>+10}".format(-300)) # -300

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
print("{0:_>+10}".format(-300))  # -300

# 3자리마다 콤마 찍어주기
print("{0:,}".format(1000000000000))

# 3자리마다 콤마 찍어주고 +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# 왼쪽정렬하고
# +- 부호도 붙이기
# 30 자릿수 확보하기 
# 3자리마다 콤마 찍어주고 , 

print("{0:^<+30,}".format(1000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))



# 파일 입출력

# "w"는 쓰기
score_file = open("score.txt", "w", encoding="utf8") #encoding은 한글사용시
print("Math : 0", file=score_file)
print("English : 50", file=score_file)
score_file.close()


# "a"는 덮어쓰기
score_file = open("score.txt", "a")
score_file.write("Science : 80")
score_file.write("\nCoding : 100")
score_file.close()


# "r"은 읽기
score_file = open("score.txt", "r")
print(score_file.read())
score_file.close()


score_file = open("score.txt", "r")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r")
print(score_file.readline(), end="")  # 줄별로 읽기
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()


score_file = open("score.txt", "r")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()


score_file = open("score.txt", "r")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()


# Pickle
# 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해 줌

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"Name":"Park", "Age":"30", "Hobby":["Soccer","Golf","Coding"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()


import pickle

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print (profile)
profile_file.close()


# With
# 좀 더 편하게 동일한 file 작업 가능

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
# with 는 따로 close 할 필요가 없다

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# 퀴즈
# 당신의 회사는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약:
# 1주차부터 10주까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

for i in range(1, 11):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")


# Class

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print(" 체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)



name = input("What is your name?")
print("{0}님 안녕하세요".format(name))
print("파이썬 강좌에 오신 것을 환영합니다")


qty = input ("사과 몇 개를 드릴까요?")
print ("사과 1개 : 500원")
print("사과 몇 개를 드릴까요?{0}".format(qty))
print ("총 금액은 {0}원입니다".format(int(qty) * 500))


a, b = input("곱셈할 두 수를 입력하세요. 예) 10 4"). split()
print ("{0} * {1} = {2:,}입니다.".format(int(a),int(b),(int(a) * int(b))))



time = input ("초를 입력해주세요.")
min = int(time) // 60
sec = int(time) % 60
print ("{0}초는 {1}분 {2}초  입니다.".format(time,min,sec))


size = float(input ("반지름을 입력해주세요."))
w = round(size * size * 3.14,2)
l = round(size * 2 * 3.14 ,2)
print ("원의 넓이는 {0:,}이고 원의 둘레는 {1:,}입니다.".format(w,l))


'''