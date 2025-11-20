## Get name from user input
# def getName():
#   name = input("What is your name? ")
#   return name
# print("Name: " + getName())



## Reverse name string
# def reverseName(name):
#   reverse = ""
#   for index in range(len(name) -1, -1, -1): # start at max, end at 0, decrease by 1
#     reverse += name[index]
#   return(reverse)
# print("Reversed Name: " + reverseName(getName()))



## Swap two variables
# def swapVariables(var1, var2):
#   temp = var1
#   var1 = var2
#   var2 = temp

#   return("Var1 = " + str(var1) + "\nVar2 = " + str(var2))
# print(swapVariables(7,6))



## Multiply Array Together
# def multiplyArr(arr):
#   if len(arr) == 0:
#     return 1

#   total = 1
#   for num in arr:
#     total *= num

#   return total

# print(multiplyArr([5,2,5]))



## Fizz Buzzer
# def fizzBuzzer(x):
#   if x % (3 * 5) == 0:
#     return("fizzbuzz")
#   elif x % 3 == 0:
#     return("fizz")
#   elif x % 5 == 0:
#     return("buzz")
#   else:
#     return("archer")

# print(fizzBuzzer(5))



## Nth Fibonacci
# def nthFibonacciNumber():
#   fibs = [1, 1]
#   num = int(input("Which fibonacci number do you want? "))

#   while len(fibs) < int(num):
#     length = len(fibs)
#     nextFib = fibs[length - 2] + fibs[length -1]
#     fibs.append(nextFib)

#   print(str(fibs[len(fibs) - 1]) + " is the fibonacci number at position " + str(num))

# nthFibonacciNumber()



## Search Array / List
# def searchArr(arr, val):
#   for index in arr:
#     if index == val:
#       return True
#   return False

# print(searchArr([1,2,3], 3))



## Palindrome
# def isPalindrome(string):
#   for index in range(int(len(string) / 2)):
#     if string[index] != string[len(string)-index-1]:
#       return False
#   return True
# print(isPalindrome("Thanks!"))
# print(isPalindrome("racecar"))



