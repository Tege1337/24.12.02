# minden cella zárva
cells = [False] * 400

# A szolgák parancsai
for x in range(1, 401):
    for y in range(x - 1, 400, x):
        cells[y] = not cells[y]  # Változtatja az ajtó állapotát

# Mely cellák vannak nyitva
open_cells = [x + 1 for x in range(400) if cells[x]]
print(f"Nyitott cellák: {open_cells}")
# pont a négyzetszámok lol