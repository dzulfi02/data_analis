#def add (a,b):
#    total = a+b 
#    return total

#print(add(10,5))
#jumlah = add(10,5)
#print(f"jumlah dari 10 dan 5 = {jumlah}")
#print(f"jumlah dari 10 dan 5 = {add(10,5)}")

def add (a = None,b= None):
    if a == None or b==None:
         print("parameter tidak lengkap")
         return

    total = a+b 
    return total

def substract(a = None,b= None):
    if a == None or b==None:
         print("parameter tidak lengkap")
         return

    total = a-b 
    return total

def bmi(berat = None, tinggi= None):
    if berat == None or tinggi ==None:
         print("parameter tidak lengkap")
         return

    total = berat/((tinggi/100)**2)
    return total

def bmi_check(bmi):
    if bmi <18.5:
        print("Anda termasuk kategori underweight")
    elif bmi <25:
        print("Anda termasuk kategori Normal")
    elif bmi <30:
        print("Anda termasuk kategori overweight")
    else:
        print("Anda termasuk kategori obesitas")
        