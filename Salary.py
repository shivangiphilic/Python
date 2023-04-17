s = int(input("Enter base salary: "))

if s <= 10000:
    hra = 20
    da = 80

elif s <= 20000:
    hra = 25
    da = 90

else:
    hra = 30
    da = 95

gross = s*hra/100 + s*da/100 + s
print(f"Gross salary is {gross}")
