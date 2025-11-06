# Najla Azizah Gunawan
# 2501796
# Kelas A

nama = input("Masukan Nama Anda:")
nilai_tugas = int(input("Masukan Nilai Tugas:"))
nilai_uts = int(input("Masukan Nilai UTS:"))
nilai_uas = int(input("Masukan Nilai UAS:"))
rata_rata = (nilai_tugas + nilai_uts + nilai_uas) / 3 

if (rata_rata >= 90):
    if (nilai_tugas>=60 and nilai_uts>=60 and nilai_uas >=70):
        print(f"{nama} kamu LULUS tanpa remedial")
    else:
        print(f"{nama} kamu LULUS dengan remedial")
else:
    if (rata_rata>=50):
         print(f"{nama} kamu TIDAK LULUS, boleh remedial")
    else:
        print(f"{nama} kamu TIDAK LULUS dan tidak boleh remedial")


