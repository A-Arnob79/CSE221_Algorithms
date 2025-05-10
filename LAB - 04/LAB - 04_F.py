def kings_advancement(n, x, y):
    paths = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    possible_moves = []
    for x_, y_ in paths:
        new_x = x + x_
        new_y = y + y_
        if (1<= new_x <=n) and (1<= new_y <=n): possible_moves.append((new_x, new_y))

    possible_moves.sort()
    print(len(possible_moves))
    for j in possible_moves: print(j[0], j[1])

n = int(input())
x, y = input().split()
kings_advancement(n, int(x), int(y))