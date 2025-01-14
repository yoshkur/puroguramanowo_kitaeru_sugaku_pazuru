# P.131

def route(width, height, back_y):
    if width == 1:
        return back_y if back_y == height else back_y + 2

    if height == 1:
        return 2 if back_y == 0 else 1

    total = 0
    if back_y == 0:
        for i in range(height):
            total += 2 * route(width=width - 1, height=height, back_y=i + 1)
    else:
        for i in range(back_y, height + 1):
            total += route(width=width - 1, height=height, back_y=i)
        total += route(width=width, height=height - 1, back_y=back_y - 1)

    return total


if __name__ == '__main__':
    print(route(width=6, height=6, back_y=0))
