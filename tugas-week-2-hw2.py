hasil = []

klub_a = input("Klub A : ")
klub_b = input("Klub B : ")

skor_valid = True
iteration = 0

while skor_valid:

    skor_a, skor_b = map(int, input(f"Pertandingan {iteration + 1} : ").split())

    if skor_a < 0 or skor_b < 0:
        break

    if skor_a > skor_b:
        hasil.append(klub_a)
    elif skor_b > skor_a:
        hasil.append(klub_b)
    else:
        hasil.append("Draw")

    iteration += 1


for index, value in enumerate(hasil):

    print(f"Hasil {index + 1} : {value}")

print("Pertandingan Selesai")