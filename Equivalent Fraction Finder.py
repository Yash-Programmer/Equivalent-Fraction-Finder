import time

Numerator = int(input("Enter Numerator:  "))
Denominator = int(input("Enter Denominator:  "))
print('\n===========================================Just Processing===========================================\n')
time.sleep(4.5)
if Numerator > 10:
    for i in range(2, 7):
        print(Numerator / i, '/', Denominator / i)
    for x in range(2, 7):
        print(Numerator, '/', Denominator)
else:
    for i in range(2, 11):
        print(Numerator * i, '/', Denominator * i)