def primeNumbers(number):
    ans = 0
    for num in range(2, number + 1):
        print("num in 1st for" + str(num))
        if num > 1:
           for i in range(2, num):
               print("i : "+ str(i))
               print("num in for " + str(num))
               if (num % i) == 0:
                   break
           else:
               print(num)
               ans += 1
    return ans

input = int(input("Please enter number: "))
print(primeNumbers(input))
