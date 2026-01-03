def knapsack(values, weights, capacity):
    n = len(values)

    # Membuat tabel DP
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Mengisi tabel DP
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][int(w - weights[i-1])] + values[i-1]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # Melacak item yang dipilih
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= int(weights[i-1])

    return dp[n][capacity], selected_items


# ======================
# DATA PERALATAN
# ======================
items = [
    "Kamera DSLR",
    "Lensa Tele",
    "Lensa Wide",
    "Tripod",
    "Drone Mini",
    "Baterai Cadangan",
    "Flash Eksternal",
    "Filter Lensa",
    "Tas Pelindung",
    "Cleaning Kit"
]

weights = [1.2, 2.5, 1.0, 2.8, 1.5, 0.8, 0.9, 0.3, 1.4, 0.4]
values  = [30, 28, 24, 26, 27, 18, 20, 10, 16, 8]

capacity = 12  # kapasitas tas (kg)

# ======================
# MENJALANKAN PROGRAM
# ======================
max_value, chosen_items = knapsack(values, weights, capacity)

print("===== HASIL KNAPSACK =====")
print("Nilai Manfaat Maksimum :", max_value)
print("\nPeralatan yang Dipilih:")

total_weight = 0
for i in chosen_items:
    print(f"- {items[i]} (Berat: {weights[i]} kg, Nilai: {values[i]})")
    total_weight += weights[i]

print("\nTotal Berat :", round(total_weight, 2), "kg")
