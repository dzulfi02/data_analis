index = [0,1,2,3,4,5,6]
nama= ["Alice", "Bob", "Charlie", "Edi", "Farah", "Gita", "Hasti"]
#nilai= [80, 90, 100, 80, 60, 90]

nama_slice_3_tengah = nama[2:5]
#nilai_slice_3_tengah = nilai[2:5]

print(nama_slice_3_tengah)
#print(nilai_slice_3_tengah)

#slice (mengganti data)
nama_slice_3_tengah[2] ="Clara"
#nilai_slice_3_tengah[0] = 99
print("\n SLICE")
print(nama_slice_3_tengah)
#print(nilai_slice_3_tengah)

#insert (menambahkan data baru)
nama_slice_3_tengah.insert(1, "Zara")
#nilai_slice_3_tengah.insert(1, 85)
print("\n INSERT")
print(nama_slice_3_tengah)
#print(nilai_slice_3_tengah)

#append (menambahkan data di akhir)
nama_slice_3_tengah.append("Dina")
#nilai_slice_3_tengah.append(100)
print("\n APPEND")
print(nama_slice_3_tengah)
#print(nilai_slice_3_tengah)

#Sort (mengurutkan data)
nama_slice_3_tengah.sort()
print("\n SORT")
print(nama_slice_3_tengah)

#POP (menghapus data akhir)
nama_slice_3_tengah.pop()
print("\n POP")
print(nama_slice_3_tengah)

#reverse (mengurutkan data secara terbalik)
nama_slice_3_tengah.reverse()
print("\n REVERSE")
print(nama_slice_3_tengah)

#print dengan index
#print("print dengan index")
#print("indeks -1 adalah {nama[-1]}") 
#print("Panjang data dari nama = ", len(nama))
#print(f"Nama {nama[1]} mendapatkan nilai {nilai[1]}")

#for z in range(len(nama)):
    #print(z)
    #print(f"Nama {nama[z]} mendapatkan nilai {nilai[z]}")
