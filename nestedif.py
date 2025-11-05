# Najla Azizah Gunawan
# 2501796
# Kelas A

bilangan = int(input("Masukan angka:")) 
genap = bilangan%2
ganjil = bilangan%2

if (genap ==0):
    print(f"Ini bilangan {bilangan} genap")
    if(bilangan >=0):
        print(f"bilangan {bilangan} ini adalah bilangan positif")
    else:
        print(f"bilangan {bilangan} ini adalah bilangan negatif")
else:
    print(f"Ini bilangan {bilangan} ganjil")
    if(bilangan >0):
        print(f"Bilangan {bilangan} ini adalah bilangan positif")
    elif(bilangan <0):
        print(f"Bilangan {bilangan} ini adalah bilangan negatif")
    else:
        print(f"Bilangan {bilangan} ini adalah bilangan nol")