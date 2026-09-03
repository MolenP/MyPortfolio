try:
    number = int(input("Enter number and I will divide 100 on this number:"))
    result = 100 / number
    print(f"The Result is: {result}")
except ValueError:
    print("ERROR: You didn't enter a number")
except ZeroDivisionError:
    print("ERROR: Number can't be divided by 0")
finally:
    print("Program has been ended")
