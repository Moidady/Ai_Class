x = [7, 2, 10, 13, 5, 6, 6]

y1 = 1
y2 = 2

def heuristic_search(x, y1, y2):
    for i in range (len(x)):
        if x[i] == y1 or x[i] == y2:
            return x[i]
        else:
            return 0

output = heuristic_search(x, y1, y2)
print(f"Hasil dari pencarian: {output}")
