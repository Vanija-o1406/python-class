seen_cells = {(1, 0), (1, 1)}

seen_cells.add((2, 1))
seen_cells.add((1, 0))

print(seen_cells)
print("Total cells:", len(seen_cells))
print("(2, 1) found?", (2, 1) in seen_cells)
print("(8, 8) found?", (8, 8) in seen_cells)

codes = ["W1", "W4", "W1", "W9", "W4"]

print("All codes:", codes)
print("Different codes:", set(codes))
print("Number of different codes:", len(set(codes)))

location = (6.5, 3.2)

print(location, type(location))

row, column = location
print("Row =", row, "| Column =", column)

single_value = (9,)

print(single_value, type(single_value))

visited_cells = set()

visited_cells.add((1, 1))
visited_cells.add((1, 2))
visited_cells.add((1, 3))
visited_cells.add((2, 1))
visited_cells.add((2, 2))
visited_cells.add((2, 2))
visited_cells.add((3, 1))
visited_cells.add((3, 2))

print("Visited cells:", visited_cells)
print("Distinct cells:", len(visited_cells))
print("(2, 2) visited?", (2, 2) in visited_cells)