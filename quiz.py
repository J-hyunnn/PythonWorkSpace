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

'''

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

