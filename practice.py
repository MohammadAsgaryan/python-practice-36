from datetime import date

dob = input().strip()

try:
    year, month, day = map(int, dob.split("/"))
    birth_date = date(year, month, day)
except:
    print("WRONG")
    exit()

current = date(2025,11,26)

age = current.year - birth_date.year

if (current.month, current.day) < (birth_date.month, birth_date.day):
    age -= 1
    
print(age)