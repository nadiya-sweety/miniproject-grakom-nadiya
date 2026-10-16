import matplotlib.pyplot as plt

# ====== Data koordinat (x, y) ======
badan  = [(2, 0), (8, 0), (8, 4), (2, 4)]            # badan rumah
atap   = [(1.5, 4), (8.5, 4), (5, 7)]                # atap segitiga
pintu  = [(4.4, 0), (5.6, 0), (5.6, 2.5), (4.4, 2.5)]
jendela_kiri  = [(2.7, 1.5), (3.9, 1.5), (3.9, 2.8), (2.7, 2.8)]
jendela_kanan = [(6.1, 1.5), (7.3, 1.5), (7.3, 2.8), (6.1, 2.8)]
jendela_atap  = [(4.6, 4.7), (5.4, 4.7), (5.4, 5.5), (4.6, 5.5)]


def gambar(titik, warna_isi, warna_garis="black", lw=2):
    """Gambar poligon: isi dengan fill(), garis tepi dengan plot()."""
    x = [p[0] for p in titik] + [titik[0][0]]
    y = [p[1] for p in titik] + [titik[0][1]]
    plt.fill(x, y, color=warna_isi, alpha=0.9)
    plt.plot(x, y, color=warna_garis, linewidth=lw)


plt.figure(figsize=(8, 7))
gambar(badan, "#f5deb3")
gambar(atap, "#c0392b")
gambar(pintu, "#8b4513")
gambar(jendela_kiri, "#87ceeb")
gambar(jendela_kanan, "#87ceeb")
gambar(jendela_atap, "#87ceeb")

# Gagang pintu
plt.scatter([5.3], [1.2], color="gold", s=40, zorder=5)

# Label titik sudut utama
for nama, (x, y) in {"A(2,0)": (2, 0), "B(8,0)": (8, 0),
                     "C(8,4)": (8, 4), "D(2,4)": (2, 4),
                     "E(5,7)": (5, 7)}.items():
    plt.scatter(x, y, color="black", s=25, zorder=5)
    plt.text(x + 0.15, y + 0.15, nama, fontsize=9)

plt.xlim(0, 10)
plt.ylim(0, 8)
plt.xticks(range(0, 11))
plt.yticks(range(0, 9))
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Mini Project: Rumah Sederhana dari Koordinat")
plt.grid(True, linestyle="--", alpha=0.5)
plt.gca().set_aspect("equal")
plt.show()
