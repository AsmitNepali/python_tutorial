a = 10
b = 3


try:
    print("resource open")
    print(a/b)
    x = int(input("Enter a number"))
    print(x)
    
except ZeroDivisionError as e:
    print("Plese don't divide your number by Zero",e)

except ValueError as e:
    print("Invalid value")


finally:
    print("resource closed")