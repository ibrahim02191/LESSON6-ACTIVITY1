height = float(input("ENTER YOUR HEIGHT IN CM"))
wieght = float(input("ENTER YOUR WIEGHT IN KG"))
bmi = wieght / (height / 100) ** 2
print("YOUR BMI IS :",bmi)
if bmi <= 18.4 :
    print("YOU R UNDER WIEGHT")
elif bmi <= 24.9 :
    print("YOU R HEALTHY")
elif bmi <= 29.9 :
    print("U R OVER WIEGHT")
elif bmi <= 34.9 :
    print("U R SEVEARLY OVER WIEGHT")
elif bmi <= 39.9 :
    print("U R OBESE")
else :
    print("U R SEVEARLY OBESE")