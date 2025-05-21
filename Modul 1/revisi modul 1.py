data_mahasiswa = {}
for _ in range(int(input("Jumlah mahasiswa: "))):
    nim = input("\nNIM: ")
    data_mahasiswa[nim] = {
        "nama": input("Nama: "),
        "nilai": [(input(f"  Matkul ke-{j+1}: "), float(input("  Nilai: ")))
                  for j in range(int(input("Jumlah matkul: ")))]
    }

print("\n=== Data Mahasiswa dan Rata-Rata Nilai ===")
for nim, mhs in data_mahasiswa.items():
    print(f"\nNIM     : {nim}\nNama    : {mhs['nama']}\nNilai:")
    total = 0
    for mk, nl in mhs["nilai"]:
        print(f"  {mk} = {nl}")
        total += nl
    rata2 = total / len(mhs["nilai"]) if mhs["nilai"] else 0
    print(f"Rata-rata: {rata2:.2f}")