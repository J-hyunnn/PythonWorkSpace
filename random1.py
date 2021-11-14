
'''

# random 관련 함수
# random.random() - 0.0이상 1미만의 실수를 반환
# random.randrange(1,10) - 1이상 10미만 범위의 임의의 정수를 반환
# random.choice([리스트]) - 리스트 내의 값을 랜덤으로 반환
#
# 가위 바위 보 프로그램 생성하기
# 이긴 경우, 진 경우, 비긴 경우, 잘못 낸 경우 각각 다른 결과

import random

user = input("무엇을 내시겠습니까?")
com = random.choice(["가위","바위","보"])

# print (type(user))
# print (type(com))


if (user == "가위") & (com == "가위"):
    print ("사용자는 {0}, 컴퓨터는 {1}".format(user,com))
    print ("비겼습니다.")
elif (user == "가위") & (com == "바위"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("컴퓨터가 이겼습니다.")
elif (user == "가위") & (com == "보"):
    print ("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print ("사용자가가 이겼습니다.")
elif (user == "바위") & (com == "가위"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("사용자가 이겼습니다.")
elif (user == "바위") & (com == "바위"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("비겼습니다")
elif (user == "바위") & (com == "보"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("컴퓨터가 이겼습니다.")
elif (user == "보") & (com == "가위"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("컴퓨터가 이겼습니다.")
elif (user == "보") & (com == "바위"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("사용자가 이겼습니다.")
elif (user == "보") & (com == "보"):
    print("사용자는 {0}, 컴퓨터는 {1}".format(user, com))
    print("비겼니다.")
else:
    print ("잘못 냈습니다. 종료")

# 가위 바위 보 프로그램 생성하기
# 이긴 경우, 진 경우, 비긴 경우, 잘못 낸 경우 각각 다른 결과

import random

user = input("무엇을 내시겠습니까?")
com = random.choice(["가위", "바위", "보"])

print (com)

if (user == "가위") or (user == "바위") or (user == "보"):
    if user == com:
        print("비겼습니다.")
    elif (user == "가위" and com == "보") or \
        (user == "바위" and com == "바위") or \
        (user == "보" and com == "가위"):
        print ("사용자가 {0}, 컴퓨터가 {1}을 내어 사용자가 이겼습니다.".format(user, com))
    else:
        print("사용자가 {0}, 컴퓨터가 {1}을 내어 컴퓨터가 이겼습니다.".format(user, com)) 
else:
    print ("잘못 냈습니다.")

'''
# 로또 프로그램 생성하기

import random

lotto = []

while len(lotto) <= 5:
    num = random.randrange(1,46)
    lotto.append(num)
    set(lotto)
print ("The winning numbers are {0}.".format(sorted(lotto)))

