import aritmatika as z

#print(add(10,6))
#print(f.bmi(50, 1.7))

#f.bmi_check(17)

bb = float(input("Masukkan berat badan (kg): "))
tb = float(input("Masukkan tinggi badan (cm): "))

bmi= z.bmi(bb,tb)
print("BMI kamu adalah",bmi)

z.bmi_check(bmi)