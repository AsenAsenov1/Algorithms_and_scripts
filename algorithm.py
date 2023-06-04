import random

matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

moves = [
    (-1, -2), (-2, -1),
    (-2, 1), (-1, 2),
    (1, -2), (2, -1),
    (2, 1), (1, 2)
]

position = {'row': 0, 'col': 0}
counter = 0

for i_row in range(len(matrix)):
    for i_col in range(len(matrix)):
        counter += 1
        print(f"Iteration: {counter}")
        random.shuffle(moves)
        current_row, current_col = position['row'], position['col']

        for row_col in moves:  # (x, y)
            add_row = row_col[0]  # x
            add_col = row_col[1]  # y

            new_row = current_row + add_row
            new_col = current_col + add_col

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if matrix[new_row][new_col] == 0:
                    matrix[new_row][new_col] = counter
                    position['row'] = new_row
                    position['col'] = new_col
                    break
            else:
                continue

        [print(x) for x in matrix]
        print()

result = []
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 0:
            result.append(0)

if len(result) == 0:
    print("SUCCESS! YOU FILLED ALL EMPTY SPACES")
else:
    print(f"Unfilled slots left: {len(result)}")
