import matplotlib.pyplot as plt

# 1. Daftar titik: (x, y, label, warna)
titik = [
    (1, 2, 'A', 'red'),
    (3, 4, 'B', 'blue'),
    (5, 1, 'C', 'green'),
    (4, 3, 'D', 'orange'),
    (2, 5, 'E', 'purple'),
]

# 2. Pisahkan koordinat, label, dan warna
x = [t[0] for t in titik]
y = [t[1] for t in titik]
label = [t[2] for t in titik]
warna = [t[3] for t in titik]

# 3. Buat figure dan axis, lalu gambar titik dengan scatter
plt.figure(figsize=(6, 5))
plt.scatter(x, y, c=warna, s=100)

# 4. Tambahkan label koordinat dan nama pada setiap titik
for (xi, yi, lab, _) in titik:
    plt.annotate(f'{lab}({xi}, {yi})', (xi, yi),
                 textcoords='offset points', xytext=(5, 5), fontsize=12)

# 5. Atur tampilan grafik: batas sumbu, tick, label sumbu, judul, grid
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xticks(range(0, 7, 1))
plt.yticks(range(0, 7, 1))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualisasi Beberapa Titik pada Bidang Koordinat')
plt.grid(True, linestyle='--', alpha=0.7)

# 7. Tampilkan hasil
plt.show()
