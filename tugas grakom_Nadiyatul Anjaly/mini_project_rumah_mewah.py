import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 8))


def poligon(titik, isi, garis="#3b2f2f", lw=1.5, z=2, alpha=1.0):
    """Poligon dari daftar koordinat: fill() untuk isi, plot() untuk tepi."""
    x = [p[0] for p in titik] + [titik[0][0]]
    y = [p[1] for p in titik] + [titik[0][1]]
    ax.fill(x, y, color=isi, alpha=alpha, zorder=z)
    ax.plot(x, y, color=garis, linewidth=lw, zorder=z + 0.1)


def persegi(x1, y1, x2, y2, isi, **kw):
    poligon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], isi, **kw)


# ================= LATAR =================
persegi(-2, 0, 24, 14, "#bfe3f7", garis="none", z=0)        # langit
persegi(-2, -1, 24, 0, "#5fae5f", garis="none", z=0.5)       # rumput
ax.add_patch(plt.Circle((20.5, 12), 1.1, color="#ffd54a", zorder=1))  # matahari
for cx, cy in [(4, 12), (11, 12.8), (16, 11.5)]:             # awan
    for dx, r in [(-0.8, 0.7), (0, 0.95), (0.9, 0.7)]:
        ax.add_patch(plt.Circle((cx + dx, cy), r, color="white", zorder=1))

# ================= JALAN SETAPAK =================
poligon([(9.2, 0), (12.8, 0), (13.6, -1), (8.4, -1)], "#d9c7a3", z=1)
poligon([(9.6, 1.2), (12.4, 1.2), (12.8, 0), (9.2, 0)], "#d9c7a3", z=1)

# ================= SAYAP KIRI & KANAN (lantai 1-2) =================
for sisi in [(2, 8.5), (13.5, 20)]:
    x1, x2 = sisi
    persegi(x1, 0.8, x2, 5.8, "#f3e6cf")                        # badan
    poligon([(x1 - 0.4, 5.8), (x2 + 0.4, 5.8), (x2 - 0.6, 7.6), (x1 + 0.6, 7.6)],
            "#8e2f2f")                                           # atap sayap

# ================= BANGUNAN TENGAH (3 lantai) =================
persegi(8.5, 0.8, 13.5, 9.0, "#fff3dc")
poligon([(8.0, 9.0), (14.0, 9.0), (11, 11.8)], "#6e1f1f", lw=2)  # atap utama
ax.add_patch(plt.Circle((11, 9.9), 0.5, color="#87ceeb", ec="#3b2f2f", lw=1.5, zorder=3))
persegi(12.3, 10.4, 12.9, 12.3, "#a65d4a")                       # cerobong

# ================= PILAR EMAS DI TERAS =================
persegi(8.0, 0.8, 14.0, 1.2, "#cfa94a")                          # lantai teras
persegi(8.3, 6.2, 13.7, 6.5, "#cfa94a")                          # balkon atas
for px in [8.7, 9.9, 12.1, 13.3]:
    persegi(px - 0.15, 1.2, px + 0.15, 6.2, "#e8c76a", lw=1)
    persegi(px - 0.25, 6.2, px + 0.25, 6.4, "#cfa94a", lw=1)
# pagar balkon
persegi(8.3, 6.5, 13.7, 7.1, "none", garis="#cfa94a", lw=1)
for bx in np.arange(8.5, 13.6, 0.5):
    ax.plot([bx, bx], [6.5, 7.1], color="#cfa94a", linewidth=1, zorder=3)

# ================= PINTU UTAMA =================
persegi(10.2, 1.2, 11.8, 4.4, "#5b3a29", lw=2)
poligon([(10.2, 4.4), (11.8, 4.4), (11, 5.2)], "#5b3a29", lw=2)
ax.plot([11, 11], [1.2, 4.4], color="#cfa94a", linewidth=1.5, zorder=4)
ax.scatter([10.8, 11.2], [2.7, 2.7], color="gold", s=25, zorder=5)

# ================= JENDELA =================
def jendela(x, y, w=1.2, h=1.8):
    persegi(x, y, x + w, y + h, "#9fd8f2", lw=1.5, z=3)
    ax.plot([x + w / 2, x + w / 2], [y, y + h], color="#3b2f2f", lw=1, zorder=4)
    ax.plot([x, x + w], [y + h / 2, y + h / 2], color="#3b2f2f", lw=1, zorder=4)
    persegi(x - 0.1, y - 0.15, x + w + 0.1, y, "#cfa94a", lw=1, z=4)  # ambang


for x in [3.0, 5.2, 14.8, 17.0]:        # lantai 1 sayap
    jendela(x, 2.0)
for x in [3.0, 5.2, 14.8, 17.0]:        # lantai 2 sayap
    jendela(x, 4.0, h=1.4)
for x in [9.0, 12.0]:                   # lantai 3 tengah
    jendela(x, 7.2, w=1.0, h=1.4)
jendela(10.5, 7.2, w=1.0, h=1.4)

# ================= PAGAR & GERBANG =================
for fx in np.arange(-1.5, 23.5, 0.6):
    if 9.0 < fx < 13.0:
        continue                         # celah gerbang
    persegi(fx, -0.2, fx + 0.12, 0.9, "#ffffff", lw=0.8, z=3)
    poligon([(fx, 0.9), (fx + 0.12, 0.9), (fx + 0.06, 1.1)], "#ffffff", lw=0.8, z=3)
ax.plot([-1.5, 9], [0.4, 0.4], color="#ffffff", lw=2, zorder=3)
ax.plot([13, 23.5], [0.4, 0.4], color="#ffffff", lw=2, zorder=3)
persegi(8.8, -0.2, 9.3, 1.8, "#bdbdbd", z=3)                     # tiang gerbang
persegi(12.7, -0.2, 13.2, 1.8, "#bdbdbd", z=3)

# ================= POHON & SEMAK =================
for tx in [0.5, 22]:
    persegi(tx - 0.2, 0.8, tx + 0.2, 3.2, "#6b4226", z=2)
    for dx, dy, r in [(0, 4.0, 1.3), (-0.8, 3.4, 0.9), (0.8, 3.4, 0.9)]:
        ax.add_patch(plt.Circle((tx + dx, dy), r, color="#2e7d32", zorder=2))
for sx in [3, 6, 16, 19]:
    ax.add_patch(plt.Circle((sx, 0.85), 0.45, color="#388e3c", zorder=4))

# ================= TITIK-TITIK KOORDINAT UTAMA =================
titik = {"A(8.5,0.8)": (8.5, 0.8), "B(13.5,0.8)": (13.5, 0.8),
         "C(13.5,9)": (13.5, 9), "D(8.5,9)": (8.5, 9), "E(11,11.8)": (11, 11.8)}
for nama, (x, y) in titik.items():
    ax.scatter(x, y, color="red", s=22, zorder=6)
    ax.text(x + 0.15, y + 0.15, nama, fontsize=8, color="darkred", zorder=6)

ax.set_xlim(-2, 24)
ax.set_ylim(-1, 14)
ax.set_aspect("equal")
ax.set_xticks(range(-2, 25, 2))
ax.set_yticks(range(-1, 15, 2))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Mini Project: Rumah Mewah dari Koordinat", fontsize=14, weight="bold")
ax.grid(True, linestyle="--", alpha=0.25)
plt.show()
