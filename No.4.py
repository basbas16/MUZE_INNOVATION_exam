input = int(input("Please enter number: "))

def primeNumbers(number):
    ans = 0
    for num in range(2, number + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               ans += 1
    return ans
    
print(primeNumbers(input))
