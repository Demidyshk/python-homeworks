# Вариант 2
# Задание 1
n, m = map(int, input('Введите количество строк и количество столбцов через пробел: ').split())
board = []
for _ in range(n):
    board.append(input('Введите * если клетка занята и . если клетка пустая без пробелов: '))

count = 0
moves = [(-1,0),(1,0),(0,-1),(0,1)]

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            continue
        can_place = True
        for movei, movej in moves:
            ni,mj = i + movei, j + movej
            if 0 <= ni < n and 0 <= mj < m:
                if board[ni][mj] == '*':
                    can_place = False
                    break
        else:
            count += 1
print(count)