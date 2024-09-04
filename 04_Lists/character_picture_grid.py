grid = [
    [".", ".", ".", ".", ".", "."],
    [".", "O", "O", ".", ".", "."],
    ["O", "O", "O", "O", ".", "."],
    ["O", "O", "O", "O", "O", "."],
    [".", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "."],
    ["O", "O", "O", "O", ".", "."],
    [".", "O", "O", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

# print(len(grid[0]))
# print(len(grid))
# for i in range(len(grid[0])):
#     for l in range(len(grid)):
#         print(grid[i][l], end="")
#     print()
for i in range(len(grid[0])):
    for l in range(len(grid)):
        print(grid[l][i], end="")
    print()
