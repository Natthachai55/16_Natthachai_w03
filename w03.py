#BMI Calculator
#Resuls = W / H^2 => h*h
 
w = float(input("Weight (kg.)"))
h = float(input("Height (m.)"))

# BMI = w/(h/100)*(h/100)
# BMI = w/((h/100)**2)
# BMI = w/h**2 
r2 = w/((h/100)**2)
r3 = f"{r2:.4f}"

print(r3)
#print(BMI)