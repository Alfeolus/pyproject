import random
list = ["Gunting","Batu","Kertas"]
pilihan = str((input("Masukkan pilihan anda: ")))
bot = (random.choice(list))
def ai():
 print("Bot memilih",bot)

if pilihan == "Gunting" or pilihan == "gunting" and bot == "Kertas":
    ai()
    print("Anda Menang")
elif pilihan == "Gunting" or pilihan == "gunting" and bot == "Gunting":
    ai()
    print("Hasilnya seri")
elif pilihan == "Gunting" or pilihan == "gunting" and bot == "Batu":
    ai()
    print("Anda Kalah")
elif pilihan == "Batu" or pilihan == "batu" and bot == "Kertas":
    ai()
    print("Anda Kalah")
elif pilihan == "Batu" or pilihan == "batu" and bot == "Gunting":
    ai()
    print("Anda Menang")
elif pilihan == "Batu" or pilihan == "batu" and bot == "Batu":
    ai()
    print("Hasilnya seri")
elif pilihan == "Kertas" or pilihan == "kertas" and bot == "Kertas":
    ai()
    print("Hasilnya seri")
elif pilihan == "Kertas" or pilihan == "kertas" and bot == "Gunting":
    ai()
    print("Anda Kalah")
elif pilihan == "Kertas" or pilihan == "kertas" and bot == "Batu":
    ai()
    print("Anda Menang")
else:
    print("ERROR!")
