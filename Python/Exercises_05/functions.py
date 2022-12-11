#This block of code is confirming if a number is divasble into the other number
#and will return a false if it cannot be done evenly or a true if it can
#For purpose of demonstartion I have changed the 4 to 6 returning in a true respone
def divisible(numerator: int, denominator: int)->bool:
 return numerator % denominator == 0
print(divisible(30,6))