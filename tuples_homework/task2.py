n = int(input('Введите количество клеток в фигуре: '))
coordinates = []
while len(coordinates)!=n:
    chisla = input('Введите координаты клетки через пробел: ')
    if not chisla:
        break
    para = tuple(map(int,chisla.split()))
    coordinates.append(para)

perimeter = n * 4
cells = [(int(x), int(y)) for x, y in coordinates]

for r, c in cells:
    if (r - 1,c) in cells:
        perimeter -= 2
    if (r, c - 1) in cells:
        perimeter -= 2
print(perimeter)
