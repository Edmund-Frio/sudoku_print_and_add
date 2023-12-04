def print_sudoku(sudoku: list):
  for i in range(len(sudoku)):
    if i > 0 and i % 3 == 0:
      print()
    for j in range(len(sudoku[i])):
      if j > 0 and j % 3 == 0:
        print(" ", end="")
      value = sudoku[i][j]
      if value == 0:
        print("_", end=" ")
      else:
        print(value, end=" ")
    print()
  

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
  for i in range(len(sudoku)):
    if i == row_no:
      for j in range(len(sudoku[i])):
        if j == column_no:
          sudoku[i][j] = number
          
          
# def print_sudoku(sudoku: list):
#   r = 0
#   for row in sudoku:
#     s = 0
#     for character in row:
#       s += 1
#       if character == 0:
#         character = "_"
#       m = f"{character} "
#       if s%3 == 0 and s < 8:
#         m += " "
#       print(m, end="")
    
#     print()
#     r += 1
#     if r%3 == 0 and r < 8:
#       print()

# def add_number(sudoku: list, row_no: int, column_no: int, number: int):
#   sudoku[row_no][column_no] = number
    



if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  print_sudoku(sudoku)
  print(add_number(sudoku, 0, 0, 2))
  print(add_number(sudoku, 1, 2, 7))
  print(add_number(sudoku, 5, 7, 3))
  print()
  print("Three numbers added:")
  print()
  print_sudoku(sudoku)
