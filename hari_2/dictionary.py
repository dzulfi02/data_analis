import json
data = {
    "nama depan": "Alice",
    "nama belakang" : "Wonder",
    "alamat" : "Bumijo",
    "umur" : 24,
    "hobi" : ["Padel", "tenis", "tenis meja"],
}

#print(data)
#print("\nSebelum diubah diubah")
#print(data ["alamat"])
#data["alamat"] ="Jogja"
#print("\nSetelah diubah")
#print(data ["alamat"])

bigdata =[
    {"nama depan": "Alice",
    "nama belakang" : "Wonder",
    "alamat" : "Bumijo",
    "umur" : 24,
    "hobi" : ["Padel", "tenis", "tenis meja"],
    },
    {
    "nama depan": "Bob",
    "nama belakang" : "Marley",
    "alamat" : "Jetis",
    "umur" : 20,
    "hobi" : ["Renang", "joging", "masak"],
    },
    {
    "nama depan": "Farah",
    "nama belakang" : "Queen",
    "alamat" : "Tugu",
    "umur" : 21,
    "hobi" : ["mukbang", "traveling", "membaca"],
    },
]

bigdata.append (
    {
    "nama depan": "Alice",
    "nama belakang" : "Wonder",
    "alamat" : "Tugu",
    "umur" : 21,
    "hobi" : ["mukbang", "traveling", "membaca"],
    }
)

print(json.dumps(bigdata, indent=4))
