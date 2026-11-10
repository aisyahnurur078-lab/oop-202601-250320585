import matplotlib.pyplot as plt

def fill_polygon(vertices):
    """Mengisi area di dalam poligon (untuk pot dan daun segitiga)."""
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)
    filled_points = []
    
    for y in range(min_y, max_y + 1):
        intersections = []
        for i in range(len(vertices)):
            x0, y0 = vertices[i]
            x1, y1 = vertices[(i + 1) % len(vertices)]
            if (y0 <= y < y1) or (y1 <= y < y0):
                if y0 != y1:
                    x_intersect = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
                    intersections.append(x_intersect)
        intersections.sort()
        for i in range(0, len(intersections) - 1, 2):
            x_start = int(round(intersections[i]))
            x_end = int(round(intersections[i+1]))
            for x in range(x_start, x_end + 1):
                filled_points.append((x, y))
    return filled_points

# 3 Bangun Datar Pembentuk Tanaman dalam Pot:
# 1. Trapesium (Pot Bunga di bagian bawah)
pot = [(40, 10), (60, 10), (65, 30), (35, 30)]

# 2. Persegi Panjang (Batang / Tangkai Tanaman)
batang = [(47, 30), (53, 30), (53, 45), (47, 45)]

# 3. Segitiga (Daun Tanaman yang Rimbun di atas)
daun = [(30, 45), (70, 45), (50, 75)]

# Dapatkan titik isi untuk masing-masing bangun datar
filled_p = fill_polygon(pot)
filled_b = fill_polygon(batang)
filled_d = fill_polygon(daun)

# Pisahkan koordinat X dan Y untuk plotting
xp, yp = zip(*filled_p) if filled_p else ([], [])
xb, yb = zip(*filled_b) if filled_b else ([], [])
xd, yd = zip(*filled_d) if filled_d else ([], [])

# Tampilkan hasil gambar penuh warna
plt.figure(figsize=(6, 6))
plt.scatter(xp, yp, color='black', s=15, marker='s', label='1. Pot (Trapesium)')
plt.scatter(xb, yb, color='saddlebrown', s=15, marker='s', label='2. Batang (Persegi Panjang)')
plt.scatter(xd, yd, color='forestgreen', s=15, marker='s', label='3. Daun (Segitiga)')

plt.title("Gambar Tanaman dalam Pot dari 3 Bangun Datar")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.3)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()