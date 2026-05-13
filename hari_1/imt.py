bb = float(input("Masukkan berat badan (kg): "))
tb = float(input("Masukkan tinggi badan (m): "))

bmi = bb/((tb/100)**2)
# print(f"BMI kamu adalah {bmi}")
# print(f"BMI kamu adalah {bmi : .2f}")
print("BMI kamu adalah " + str(bmi))

if bmi <18.5:
    print("Anda termasuk kategori underweight")
elif bmi <25:
    print("Anda termasuk kategori Normal")
elif bmi <30:
    print("Anda termasuk kategori overweight")
else:
    print("Anda termasuk kategori obesitas")