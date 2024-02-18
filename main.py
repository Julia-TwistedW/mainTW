for x in range(1, 1000):
    for y in range(1, 1000):
            a = (((x % 7) == 0) <= (((x % 21 )!= 0))) or (2 * x + (y >= 120))
            if a == 1:
                print(x, y)


