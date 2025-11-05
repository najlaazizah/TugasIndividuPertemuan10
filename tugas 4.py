# Najla Azizah Gunawan
# 2501796
# Kelas A

jenis_kelamin = input("Masukkan jenis kelamin: ").lower()
umur = int(input("Masukkan umur: "))
tinggi = int(input("Masukkan tinggi badan (cm): "))
iq = int(input("Masukkan IQ: "))

if (18 <= umur <= 25):
    if (jenis_kelamin == "wanita" and tinggi >= 170 and iq >= 130):
        print("Anda memenuhi syarat menjadi model catwalk (wanita).")
    elif (jenis_kelamin == "pria" and tinggi >= 175 and iq >= 130):
        print("Anda memenuhi syarat menjadi model catwalk (pria).")
    else:
        print("Maaf, Anda belum memenuhi semua kriteria model catwalk.")
else:
    print("Maaf, umur Anda tidak memenuhi syarat (harus 18–25 tahun).")
