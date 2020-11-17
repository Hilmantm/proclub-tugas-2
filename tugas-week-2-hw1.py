arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    bMin = arrBerat[0]

    for i in arrBerat:
        if i > bMax:
            bMax = i

        if i < bMin:
            bMin = i


def rerata(arrBerat):
    result = 0
    for i in arrBerat:
        result += i
    return result / len(arrBerat)


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')

    # Inisialisasi Input Data Berat
    berat = float(input())

    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(berat)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print(f"Berat balita minimum: {bMin:.2f} kg")
print(f"Berat balita maksimum: {bMax:.2f} kg")
print(f"Rerata berat balita: {rerata(arrBerat):.2f} kg")


