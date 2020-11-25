print("enter date of birth")
birthyear=int(input("enter the year:"))
birthmonth=int(input("enter the month:"))
birthday=int(input("enter the day:"))
print("enter current date")
currentyear=int(input("enter the year:"))
currentmonth=int(input("enter the month:"))
currentday=int(input("enter the day:"))

if currentmonth>birthmonth:
    age=currentyear-birthyear
else:
    age=currentyear-birthyear-1
if currentmonth==birthmonth:
    if currentday>=birthday:
        age=currentyear-birthyear
    else:
        age = currentyear - birthyear-1
print("age is ",age)

