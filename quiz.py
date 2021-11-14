'''
# 1.
# Open a kr.csv and print it's contents.

files = open("kr.csv", "r")
while True:
    file = files.readline()
    if not file:
        break
    print(file)

files.close()



# 2
# You can get 10% discount when you spend more than 10000 won

saleprice = int(input("What is your purchaing price? "))
if saleprice >= 10000:
    discount = round(saleprice * 0.1,2)
    print("Purchaing price : {0} won".format(saleprice))
    print("Discount : {0} won".format(discount))
    print("Payment amount : {0} won".format(saleprice-discount))
else:
    print("You do not get any discount!")



# 3
# You can ride the rides when your are over 12 years old and over 120cm tall.

age = int(input("How old are you?"))
tall = int(input("How tall are you? cm"))

if (age >= 12) and (tall >=120):
    print ("You can ride it, Enjoy!")
else:
    print ("You CAN NOT ride it!")


# 4
# Calculate age from the birth year.

birthyear = int(input("Which year were you born?"))
age = 2021 - birthyear + 1
print ("You are {0} years old.".format(age))
if (age >= 8 ) and (age <= 13):
    print ("Elementary school")
elif (age >= 14) and (age <= 16):
    print("middle school")
elif (age >= 17) and (age <= 19):
    print("high school")
elif age >= 20:
    print("adult")
else:
    print("preschool child")




# 5
# do the sum from 1 to number


sum = 0

for x in range(1,11):
    sum = sum + x
print("from 1 to 10's total sum is {0}".format(sum))



# 5-1

lastNo = int(input("please give me a number."))
i = 1
sum = 0
while i <= lastNo:
    sum = sum + i
    i += 1
print (sum)



# 6 calculate odd number from 1 to 10

oddNo=0

for i in range(1,10,2):

    oddNo = oddNo + i 

print ("Total sum of odd number from 1 and 10 is {0}".format(oddNo))



# 6-1

oddNo = 0

for i in range(1, 10):
    if (i % 2 == 1):
        print (i)
        oddNo = oddNo + i
        i += 1

print("Total sum of odd number from 1 and 10 is {0}".format(oddNo))



i = 1
sum = 0

while i <= 9:
    if i % 2 == 1:
        sum = sum + i
    i += 1

print (sum)


# Viktors
sum = 0
for x in range(10):
    if x % 2 == 1:
        sum = sum + x

print(sum)

'''

