from boolisLeapYear import boolisLeapYear

inputYear = input("What year do you want to check whether is leap year or not? ")

if boolisLeapYear(int(inputYear)):
    print(str(inputYear) + " is a leap year")
else:
    print(str(inputYear) + " is not a leap year")
