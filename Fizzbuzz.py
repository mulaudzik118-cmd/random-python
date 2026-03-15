def ThreeDivisibleChecker(y):
    number = y 
    div_3 = number % 3
    isdivby3 = False
    match div_3:
        case 0:
            isdivby3 = True
    return isdivby3

def FiveDivisibleChecker(y):
    number = y 
    div_5 = number % 5
    isdivby5 = False
    match div_5:
        case 0:
            isdivby5 = True
    return isdivby5

def FizzbuzzGame(y):
         isFizz = None
         isBuzz = None
         isFizzBuzz = None
         if  ThreeDivisibleChecker(y):
           if FiveDivisibleChecker(y):
            isFizzBuzz = True
            
           elif ThreeDivisibleChecker(y):
            isFizz = True

         if FiveDivisibleChecker(y):
           if ThreeDivisibleChecker(y):
               isFizzBuzz = True

           elif FiveDivisibleChecker(y):
               isBuzz = True
        
         if isFizz == True:
             print("Fizz")

         elif isBuzz == True:
             print("buzz")

         elif (isFizzBuzz == True):
             print("Fizzbuzz")

         if (ThreeDivisibleChecker(y) == False) and (FiveDivisibleChecker(y) == False):
             print(x)
             
        


print ("Enter min number")
minNum = int(input())
print ("Enter max number")
maxNum = int(input())
maxNum = int(maxNum+1)

for x in range(minNum, maxNum):
   FizzbuzzGame(x)
   


# First step is to count to the max number
#Second step is to 