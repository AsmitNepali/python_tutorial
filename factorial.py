def factorial(n):
    f = 1

    for i in range(1,n+1):
        f = f*i
    return f


num = int(input("Enter interger."))

resutl = factorial(num)

print("The factorial {} is {}".format(num,resutl))

