

import matplotlib.pyplot as plt

# 1. Titik-titik (vertex) setiap poligon
segitiga = [(1, 1), (4, 1), (2.5, 4)]
persegi = [(6, 1), (8, 1), (8, 3), (6, 3)]
segi_lima = [(1, 5), (2, 7), (4, 7), (5, 5), (3, 4)]


# 2. Pisahkan koordinat x dan y
def get_xy(titik):
    x = [p[0] for p in titik]
    y = [p[1] for p in titik]
    return x, y


# 3. Buat figure
plt.figure(figsize=(8, 6))

# 4. Gambar segitiga (garis + isian)
x, y = get_xy(segitiga)
plt.fill(x, y, color='red', alpha=0.3)
plt.plot(x + [x[0]], y + [y[0]], color='red', linewidth=2, marker='o')
plt.text(2.5, 4.3, 'Segitiga', ha='center')

# 5. Gambar persegi
x, y = get_xy(persegi)
plt.fill(x, y, color='blue', alpha=0.3)
plt.plot(x + [x[0]], y + [y[0]], color='blue', linewidth=2, marker='o')
plt.text(7, 3.3, 'Persegi', ha='center')

# 6. Gambar segi lima
x, y = get_xy(segi_lima)
plt.fill(x, y, color='green', alpha=0.3)
plt.plot(x + [x[0]], y + [y[0]], color='green', linewidth=2, marker='o')
plt.text(3, 7.3, 'Segi Lima', ha='center')

# 7. Atur tampilan grafik
plt.xlim(0, 9)
plt.ylim(0, 8)
plt.xticks(range(0, 10, 1))
plt.yticks(range(0, 9, 1))
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualisasi Poligon dengan Python')

# 9. Tampilkan hasil
plt.show()
